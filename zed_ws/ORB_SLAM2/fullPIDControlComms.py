#!/usr/bin/env python
#
# This program defines the twist and accelerator control
# the actual velocity is calculated by a stereo camera
# it reads a map, created previusly
#
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import rospy
import time
import numpy as np
import serial
import serial.tools.list_ports
import warnings
import sys, select, os
import itertools
import math
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int16

zed_pos_x_ = 1.0 # initializes zed x position variable
zed_pos_y_ = 1.0 # initializes zed y position
zed_theta_ = 0.0 # initializes zed theta orientation
time_stamp = 0.0 # initializes time stamps for calculating speed
gamma = 0        # initializes variables for publishers
q_acc = 0        # initializes accelerator varible for publisher
q_brake = -2     # initializes brake varible for publisher
camera_state = 1 # it the camera status
frame_id = 0
# harlan_state = 1

if os.name == 'nt':
    import msvcrt
else:
    import tty, termios

#reemplazar port='/dev/tty' por el puerto al que este conectado el PLC
client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=0.07, stopbits=1, bytsize=8, parity='N', baudrate=9600)
#En caso de no estar conectado al PLC, el programa arrojara un error en esta linea debido a que es la encargada de la comunicacion
client.connect()

e = """
Communications Failed
"""

#client.read_discrete_inputs(n,1,unit=5)
#client.read_input_registers(address,number_of_registers_to_read, unit=5)

# acc_sp = 0
# brk_sp = 9
# direction = 4

# NOM - 194-SCFI - 2015

#This is for getting published pose from node
def callback_pose(data):
    global zed_pos_x_ # position of x axis of the stereo camera
    global zed_pos_y_ # position of y axis of the stereo camera
    global zed_theta_ # orientation of the stereo camera
    global time_stamp # its the time it takes beetwen cycles
    zed_pos_x_ = data.pose.position.x       # data is argument for callback, pose is data attribute
    zed_pos_y_ = data.pose.position.y       # position/orientation is pose attribute
    zed_theta_ = data.pose.orientation.y    # angle data from stereo camera
    time_stamp = data.header.stamp.nsecs    #timestamp from position in nanoseconds

def callback_state(data):
    global camera_state         # status of lost trackin or actual position
    camera_state = data.data    # data argument for camera lostcall

# Function in charge of reading an extern file that cotains the data of the map
# this data is fill with coordinates x,y and angle, also it cotains the time_stamp variable
# this function also puts this info into a buffer
# @return values its a buffer of frames from the whole map

# this method converts the txt file to a matrix float (nested lists) for data usage
# and comparing values
def getfile():
    rfile = open("KeyFrameTrajectory_TUM_Format.txt", "r")  # open the text file that contains all the track points data
    rfile = rfile.read()                            # rfile.read() opens the txt file to be read
    rfile = rfile.split("\n")                       # separates the text of the file every enter
    values = []                                     # initialize values array
    fileRows = len(rfile)                           # gets the numer of rows in the file
    count = 0                                       # auxiliary counter for getting just the floats on the file and not strings
    for item in rfile:                              # iteration that firs divides all the text file in rows
        buffer = []                                 # and then spaces different values divided by spaces
        if count == fileRows - 1:                   # breaking the for loop when it reaches the end of the file length
            break                                   #
        elif count == 0:                            # for deleting the headers of the txt file
            print("Program Running... ")            #
        else:                                       #
            for element in item.split(" "):         #
                buffer.append(element)              # appends every number to the current matrix row
                buffer = [float(i) for i in buffer] # converts the string type data to float on the buffer array
            buffer.pop(0)
            values.append(buffer)
        count += 1
    return (values)

last_time_stamp = 0     # initialize the varible used as a previous time_stamp
delta_time = 0.1        # initialize the varible in charge of the time lapse
speed_d = 0             # initialize the varible in charge of the velocity vector
last_zed_pos_x_ = 0     # initialize the varible used as a previous x_coordinate
last_zed_pos_y_ = 0     # initialize the varible used as a previous y_coordinate

curve = 0                   # initialize the varible that represents whether its a curve or not
start_curve_frames = []     # initialize a buffer that will contain numbers of frame where a curve starts
end_curve_frames = []       # initialize a buffer that will contain the number of the frame where a curve ends

# Function in charge of filling the buffers mentioned before
# that can tell whether you're on a curve or not
# @param values represents buffer of whole map in frames
# @return start_curve_frames and end_curve_frames filling with the curves

def curve_id (values):
    global start_curve_frames       # the varible that will register when the curve starts
    global end_curve_frames         # the varible that will register when the curve ends
    global curve                    # varible that represents whether its a curve or not
    count_start = 0                 # frame counter for initializing curves
    count_end = 0                   # frame counter for ending curves
    n = 0
    for b in values:
        if type(b)==type([]):
            n+=1
    for i in range(n):
        difference_theta = values[i][3]         # save all values of the third column from text file: KeyFrameTrajectory_TUM_Format.txt
        if(difference_theta>1):                 # doing a comparation to know where is the beginning of the curve from all values
            count_start += 1                    # counter starts
            # print 'count', count_start
            if count_start == 5:                                # if the condition is true 5 times, the program will identify the beginning of the curve
                curve = 1                                       # the program identifies if you are in the curve in real time
                start_curve_frames.append(i-count_start+1)      # frames identificated as the beginning of the curves
                count_end = 0                                   # reset count_end
        elif (difference_theta < 1):                            # doing a comparation to know where is the ending of the curve from all values
            count_end += 1                                      # counter starts
            if count_end == 5:                                  # if the condition is true 5 times, the program will identify the ending of the curve
                curve = 0                                       # the program identifies if your aren't in the curve in real time
                end_curve_frames.append(i-count_end+1)          # frames identificated as the ending of the curves
                count_start = 0                                 # reset count_start
    end_curve_frames.pop(0)
    print 'start_curve_frames ', start_curve_frames
    print 'end_curve_frames ', end_curve_frames

# Function incharge of finding the nearest key frame
# @param values is the array of data

def nearKeyFrame(values):
    global gamma    # Is the value of the stearing wheel
    global q_acc    # Is the value of the accelerator pedal
    global q_brake  # Is the value of the brake pedal
    n=0
    global last_time_stamp  # Is the time enlapse
    global frame_id
    for b in values:
        if type(b)==type([]):
            n+=1
    error_list = []
    # condition = 0
    print 'Finding in route...'
    print 'Press Ctrl + C to kill process'
    # gamma = 5
    q_acc = 0
    q_brake = 9
    pub_gamma = rospy.Publisher('control_gamma', Int16, queue_size=10)
    pub_acc = rospy.Publisher('accelerator', Int16, queue_size=10)
    pub_brk = rospy.Publisher('brakes', Int16, queue_size=10)
    pub_gamma.publish(gamma)
    pub_acc.publish(q_acc)
    pub_brk.publish(q_brake)
    time.sleep(1)
    while not rospy.core.is_shutdown():
        rospy.Subscriber('ORB_SLAM2/pose', PoseStamped, callback_pose)
        while frame_id < n - 1 and zed_pos_x_ != 1 and zed_pos_y_ != 1:
            # if rospy.core.is_shutdown():
            x_coordinate = values[frame_id][0]
            y_coordinate = values[frame_id][1]
            error_x = zed_pos_x_ - x_coordinate
            error_y = zed_pos_y_ - y_coordinate
            error_d = math.sqrt(error_x*error_x + error_y*error_y)
            error_list.append(error_d)
            frame_id += 1
        if last_time_stamp != time_stamp:
            last_time_stamp = time_stamp
            minValue = min(error_list)
            frame_id = error_list.index(minValue)
            return frame_id
        else:
            frame_id = 0
            error_list = []

def gamma_comtrol(error):
    if error < -28:
        gamma = 0
    elif error >= -28 and error < -21:
        gamma = 1
    elif error >= -21 and error < -14:
        gamma = 2
    elif error >= -14 and error < -7:
        gamma = 3
    elif error <= 0 and error > -7:
        gamma = 4
    elif error > 0 and error < 7:
        gamma = 5
    elif error >= 7 and error < 14:
        gamma = 6
    elif error >= 14 and error < 21:
        gamma = 7
    elif error >= 21 and error < 28:
        gamma = 8
    elif error >= 28 and error < 35:
        gamma = 9
    elif error >= 35:
        gamma = 10
    return gamma

def acc_control(error):
    if error < 0:
        acc_sp = 0
    elif error >= 0 and error < 1:
        acc_sp = 1
    elif error >= 1 and error < 2:
        acc_sp = 2
    elif error >= 2 and error < 3:
        acc_sp = 3
    elif error >= 3 and error < 4:
        acc_sp = 4
    elif error >= 4 and error < 5:
        acc_sp = 5
    elif error >= 5 and error < 6:
        acc_sp = 6
    elif error >= 6 and error < 7:
        acc_sp = 7
    elif error >= 7 and error < 8:
        acc_sp = 8
    elif error >= 9:
        acc_sp = 9
    return acc_sp

def brk_control(error):
    if error > 2:
        brake_sp = 9
    elif error >= 1 and error < 2:
        brake_sp = 8
    elif error >= 0 and error < 1:
        brake_sp = 7
    elif error >= -1 and error < 0:
        brake_sp = 6
    elif error >= -2 and error < -1:
        brake_sp = 5
    elif error >= -3 and error < -2:
        brake_sp = 4
    elif error >= -4 and error < -3:
        brake_sp = 3
    elif error >= -5 and error < -4:
        brake_sp = 2
    elif error >= -6 and error < -5:
        brake_sp = 1
    elif error < -6:
        brake_sp = 0
    return brake_sp

def controlComm():
    rospy.init_node('listener', anonymous=True)
    # rospy.init_node('listener', anonymous=True)
    last_error_theta = 0.0 # initializes a thetha variable
    last_error_speed = 0.0 # initializes a speed variable
    integral_theta = 0.0
    integral_speed = 0.0
    next_frame_stop = 0  # initailizes a stop varible
    on_curve = 0
    speed_sp = 5.0
    speed_error= 0
    output_gamma = 5
    output_brk = 0
    output_acc = 0
    at_stop = 0
    aux = 0
    values = getfile() # readsfile and stores in dynamic array
    curves = curve_id(values)
    frame_id = nearKeyFrame(values) # gets nearest keyframe to actual position
    global last_time_stamp
    global last_zed_pos_x_
    global last_zed_pos_y_
    global gamma
    print "Connected"
    print "K to stop control, Ctrl + C to kill program"
    print 'ok1'

    for curve_index in range(len(start_curve_frames) - 1):
        if frame_id >= start_curve_frames[curve_index]:
            nearest_curve_id = start_curve_frames[curve_index - 1]
            break
        else:
            nearest_curve_id = start_curve_frames[0]

    print 'nearest_curve_id', nearest_curve_id

    client.write_coil(65,True,unit=5) # subrutinas y prender el plc
    # client.write_coil(60,True,unit=5) # accelerator
    client.write_coil(57,True,unit=5) # brakes
    client.write_coil(58,True,unit=5) # Energizar direccion
    print 'Control Running...'
    rate = rospy.Rate(10) # rate at which the node publishes in Hz
    time.sleep(1)

    # pub_gamma = rospy.Publisher('control_gamma', Int16, queue_size=10) # publisher for controlling the steering wheel
    # pub_acc = rospy.Publisher('accelerator', Int16, queue_size=10) # publisher for controlling the accelerator
    # pub_brk = rospy.Publisher('brakes', Int16, queue_size=10) # publisher for controlling the brakes
    # pub_stop = rospy.Publisher('stopRoutine', Int16, queue_size=10)

    while not rospy.core.is_shutdown():
        # Ctrl + C shuts program down


        set_stop = client.read_coils(11,1,unit=5)
        reset_stop = client.read_coils(12,1,unit=5)
        emergency = client.read_coils(8,1,unit=5)
        directionPLC = client.read_input_registers(3,1,unit=5) # reads direction position from PLC
        brakesPLC = client.read_input_registers(7,1,unit=5) # reads brakes position from PLC
        upbrk = client.read_coils(96,1,unit=5)
        dwnbrk = client.read_coils(97,1,unit=5)

        rospy.Subscriber('ORB_SLAM2/pose', PoseStamped, callback_pose) #(Node, msg, callback_function)
        rospy.Subscriber('ORB_SLAM2/Camera_State', Int16, callback_state)

        desired_x = values[frame_id][0]
        desired_y = values[frame_id][1]

        error_x = desired_x - zed_pos_x_ # error en componente x en  m
        error_y = desired_y - zed_pos_y_ # error en componente y en m
        error_d = math.sqrt(error_x**2 + error_y**2)
        x_prime = error_x*math.cos(zed_theta_*math.pi/180) - error_y*math.sin(zed_theta_*math.pi/180)
        y_prime = error_x*math.sin(zed_theta_*math.pi/180) + error_y*math.cos(zed_theta_*math.pi/180)
        theta = math.atan(x_prime/y_prime)*180/math.pi

        x_to_next_curve = values[nearest_curve_id][0] - zed_pos_x_
        y_to_next_curve = values[nearest_curve_id][1] - zed_pos_y_
        d_to_next_curve = math.sqrt(x_to_next_curve**2 + y_to_next_curve**2)

        brakesRoutine = client.read_coils(57,1,unit=5)

        if set_stop.bits[0] == True:
            next_frame_stop = frame_id
            aux = 1
        elif reset_stop == True:
            aux = 0

        if last_time_stamp != time_stamp:
            # print 'Last time stamp: ', last_time_stamp
            if last_time_stamp > time_stamp:
                delta_time = (time_stamp + 10**9) - last_time_stamp
            else:
                delta_time = (time_stamp - last_time_stamp) #conversion to seconds
            # print(delta_time)
            # print(' ')
            speed_x = (3.6*(zed_pos_x_-last_zed_pos_x_)/(delta_time))*10**9 # m/s
            speed_y = (3.6*(zed_pos_y_-last_zed_pos_y_)/(delta_time))*10**9 # m/s
            speed_d = math.sqrt(speed_x**2 + speed_y**2)
            last_zed_pos_x_ = zed_pos_x_
            last_zed_pos_y_ = zed_pos_y_
            last_time_stamp = time_stamp

            if (d_to_next_curve) < 1 or gamma > 7 or gamma < 3:
                on_curve = 1
                speed_sp = 2.0
            elif (frame_id)  > end_curve_frames[curve_index]:
                on_curve = 0
                speed_sp = 4.0
                if curve_index == len(end_curve_frames)- 1:
                    curve_index = 0
                else:
                    curve_index += 1
                nearest_curve_id = start_curve_frames[curve_index]

            speed_error = speed_sp - speed_d

            kp_gamma = 0.180 # jugar experimentalmente
            kp_acc = 0.1  # jugar experimentalmente
            kp_brk = 1    # jugar experimentalmente

            ki_gamma = 0.015
            ki_acc = 0.001
            ki_brk = 0.1

            kd_gamma = 2.3
            kd_acc = 0.1
            kd_brk = 0.1


            if camera_state == 2: #  camera lost
                print 'lost'
                client.write_register(20, 0, unit=5)
                frame_id = nearKeyFrame(values)

            elif emergency.bits[0] != True: # camera not lost and no emergency on PLC
                if frame_id >= (next_frame_stop - 6) and frame_id <= (next_frame_stop + 6) and aux == 1:
                     # camera not lost and no emergency on PLC and at stop point
                    print 'Stop at post'
                    client.write_coil(8, True, unit=5) # turns emergency.bits[0] to true
                    at_stop = 1
                    frame_id += 7
                    # pub_stop.publish(1)
                else: # camera not lost and no emergency on PLC and not at stop point
                    # else continue control
                    at_stop = 0
                    output_gamma = kp_gamma*theta + ki_gamma*integral_theta + kd_gamma*(theta-last_error_theta)
                    output_acc = kp_acc*speed_error
                    output_brk = kp_brk*speed_error + ki_brk*integral_speed + kd_brk*(speed_error-last_error_speed)
                    gamma = gamma_comtrol(output_gamma)
                    q_acc = acc_control(output_acc)
                    q_brake = brk_control(output_brk)
                    # pub_stop.publish(0)
                    client.write_register(25, gamma, unit=5)
                    client.write_register(20, q_brake, unit=5)   #brakes
                    # pub_gamma.publish(1)
                    print 'Continue to next post'

            # if emergency.bits[0] == False and at_stop == 1:
            #     frame_id += 7

            # pub_gamma.publish(gamma)
            # pub_acc.publish(q_acc)
            # pub_brk.publish(q_brake)

            integral_theta += theta
            integral_speed += speed_error

            if (error_d <= 1 or y_prime < 0):
                integral_theta = 0
                #integral_speed = 0
                frame_id += 7
                if frame_id > len(values) - 5:
                    frame_id = 0

            last_error_theta = theta
            last_error_speed = speed_error

            last_gamma = gamma
            last_q_brake = q_brake

        print 'Next KeyFrame:   ', frame_id
        print 'Next Stop:       ', next_frame_stop
        print 'auxiliary:       ', aux
        # print 'x_prime:         ', x_prime
        # print 'y_prime:         ', y_prime
        # print 'Next_curve_id:   ', nearest_curve_id
        # print 'on_curve:        ', on_curve
        # print 'd_to_next_curve: ', d_to_next_curve
        print 'Speed:           ', speed_d
        print 'Speed setpoint:  ', speed_sp
        print 'Speed error:     ', speed_error
        print 'Distance Error:  ', error_d
        print 'Gamma Setpoint:  ', gamma
        print 'Direction:       ', directionPLC.registers[0]
        # print 'Acc Setpoint:    ', q_acc
        print 'Brakes Setpoint: ', q_brake
        print 'Brakes:          ', brakesPLC.registers[0]
        print 'Output gamma:    ', output_gamma
        print 'Output_brk:      ', output_brk
        print 'emergency        ', emergency.bits[0]
        print 'brakesRoutine    ', brakesRoutine.bits[0]
        print 'dwnbrk:          ', dwnbrk.bits[0]
        print 'upbrk            ', upbrk.bits[0]
        print ' '
        rate.sleep()

if __name__ == '__main__': #metodo main que arroja un exception en caso de un error en la comunicacion
    if os.name != 'nt':
        # try:
            # settings = termios.tcgetattr(sys.stdin)
            # pubRoutine = rospy.Publisher('motion_state', Int16, queue_size=10)
            # termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        # except:
        controlComm()
        # print e
    # if os.name != 'nt':
