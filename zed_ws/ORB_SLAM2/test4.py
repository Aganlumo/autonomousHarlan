#!/usr/bin/env python

import rospy
import math
import time
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int16, Float32
import matplotlib.pyplot as plt

zed_pos_x_ = 1.0
zed_pos_y_ = 1.0
zed_theta_ = 0.0
time_stamp = 0.0
gamma = 0

#This is for getting published pose from node
def callback(data):
    global zed_pos_x_
    global zed_pos_y_
    global zed_theta_
    global time_stamp

    zed_pos_x_ = data.pose.position.x #data is argument for callback, pose is data attribute
    zed_pos_y_ = data.pose.position.y #position/orientation is pose attribute
    zed_theta_ = data.pose.orientation.y
    time_stamp = data.header.stamp.nsecs #timestamp from position in nanoseconds

def getfile():
    rfile = open("KeyFrameTrajectory_TUM_Format.txt", "r")
    rfile = rfile.read()
    rfile = rfile.split("\n")
    values = []
    fileRows = len(rfile)
    count = 0
    for item in rfile:
        buffer = []
        if count == fileRows - 1:
            break
        elif count == 0:
            print("init")
        else:
            for element in item.split(" "):
                buffer.append(element)
                buffer = [float(i) for i in buffer]
            buffer.pop(0)
            values.append(buffer)
        count += 1
    return (values)

def Gabo():
    global gamma
    x_axis = zed_pos_x_
    y_axis = zed_pos_y_
    plt.scatter(x_axis, y_axis, label="POSITIONS", color="red", marker="o", s=30)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('TRAYECTORY_ZED')
    plt.legend()
    plt.show()

last_time_stamp = 0
delta_time = 0.1
speed_d = 0
speed_th = 0
last_zed_pos_x_ = 0
last_zed_pos_y_ = 0
last_d = 0
last_zed_theta_ = 0
coment_gamma = 0

def z2n(error):
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
    elif error >= 28:
        gamma = 9
    return gamma

def nearKeyFrame(values):
    n=0
    global last_time_stamp
    for b in values:
        if type(b)==type([]):
            n+=1
    global count2
    error_list = []
    condition = 0
    while condition != 1 or not rospy.core.is_shutdown():
        rospy.Subscriber('ORB_SLAM2/pose', PoseStamped, callback)
        while count2 < n - 1 and zed_pos_x_ != 1 and zed_pos_y_ != 1:
            x_coordinate = values[count2][0]
            y_coordinate = values[count2][1]
            theta_coordinate = values[count2][2]
            print zed_pos_x_
            print zed_pos_y_
            error_x = zed_pos_x_ - x_coordinate
            error_y = zed_pos_y_ - y_coordinate
            error_d = math.sqrt(error_x*error_x + error_y*error_y)
            error_list.append(error_d)
            # error_t = abs(zed_theta_ - theta_coordinate)
            print error_x
            print error_y
            # print error_t
            print 'In While', count2
            count2 += 1
            print ' '
        if last_time_stamp != time_stamp:
            last_time_stamp = time_stamp
            print error_list
            minValue = min(error_list)
            print minValue
            count2 = error_list.index(minValue)
            print count2
            print " ^^ "
            return count2
            break
            condition = 1
        else:
            count2 = 0
            error_list = []
            # print type(count2)
            # def onTheLine(): #later

last_theta = 0

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    count2 = 0
    values = getfile()
    count2 = nearKeyFrame(values)
    # count2 = int(count2)
    pub = rospy.Publisher('control_gamma', Int16, queue_size=10)
    pub1 = rospy.Publisher('speed', Float32, queue_size=10)
    pub2 = rospy.Publisher('speed_th', Float32, queue_size=10)
    rate = rospy.Rate(10)
    print ' '
    while not rospy.core.is_shutdown():
        # Gabo()
        # Ctrl + C shuts program down
        rospy.Subscriber('ORB_SLAM2/pose', PoseStamped, callback) #(Node, msg, callback_function)
        desired_x = values[count2][0]
        desired_y = values[count2][1]
        desired_t = values[count2][2]
        current_d = math.sqrt(zed_pos_x_*zed_pos_x_ + zed_pos_y_*zed_pos_y_)

        if last_time_stamp != time_stamp:
            delta_time = (time_stamp - last_time_stamp) #conversion to seconds
            # print 'Delta time: ', delta_time
            # print(delta_time)
            # print(' ')
            speed_x = (zed_pos_x_-last_zed_pos_x_)/delta_time*10**9 #m/s
            speed_y = (zed_pos_y_-last_zed_pos_y_)/delta_time*10**9 #m/s
            speed_d = (current_d-last_d)/delta_time*10**9 #m/s
            speed_th = (zed_theta_ - last_zed_theta_)/delta_time*10**9 #deg/s
            last_zed_pos_x_ = zed_pos_x_
            last_zed_pos_y_ = zed_pos_y_
            last_zed_theta_ = zed_theta_
            last_time_stamp = time_stamp
            last_d = current_d
            # print 'Actual ', time_stamp
            # print 'Last ', last_time_stamp
            # print 'Speed x: ', speed_x
            # print 'Speed y: ', speed_y

        error_x = desired_x - zed_pos_x_ # error en componente x en  m
        error_y = desired_y - zed_pos_y_ # error en componente y en m
        coment_t = desired_t - zed_theta_ # hay que modificar para cuando el angulo se acerca 180####BORRAR
        # alpha = math.atan(zed_pos_x_/zed_pos_y_)*(180/math.pi) # error de theta con respecto a la posicion
        error_d = math.sqrt(error_x*error_x + error_y*error_y)
        x_prime = error_x*math.cos(zed_theta_*math.pi/180) - error_y*math.sin(zed_theta_*math.pi/180)
        y_prime = error_x*math.sin(zed_theta_*math.pi/180) + error_y*math.cos(zed_theta_*math.pi/180)
        theta = math.atan(x_prime/y_prime)*180/math.pi

        print 'x_prime: ', x_prime
        print 'y_prime: ', y_prime

####BORRAR##############################
        if(coment_t>=300):             #
            coment_t = coment_t - 360  #
        elif (coment_t <= -300):       #
            coment_t = coment_t + 360  #
########################################

        # # quadrant 1
        # if (error_x > 0 and error_y >=  0):
        #     theta = alpha
        # # quadrant 2
        # elif (error_x < 0 and error_y > 0):
        #     theta = alpha
        # # quadrant 3
        # elif (error_x < 0 and error_y < 0):
        #     theta = alpha - 180
        # #quadrant 4
        # elif (error_x > 0 and error_y < 0):
        #     theta = alpha + 180

        if(theta>=180):
            theta = theta - 360
        elif (theta <= -180):
            theta = theta + 360

        # error_t = theta - zed_theta_

        kp = 1.0 #jugar experimentalmente
        gamma = z2n(kp*theta)
        coment_gamma = z2n(kp*coment_t)####BORRAR
        print 'To harlan (calculated): ', gamma
        print 'To harlan (keyframe): ', coment_gamma      ####BORRAR
        # print 'Speed: ', speed_d
        # print 'Angular speed: ', speed_th
        pub.publish(gamma)
        pub1.publish(speed_d)
        pub2.publish(speed_th)

        # if error_t <= -5:
        #     print 'Turn right'
        # elif error_t >= 5:
        #     print 'Turn left'
        # else:
        #     print 'Go straight'

        if (error_d <= 0.4):
            count2 += 5
            last_theta = theta
            if count2 > len(values) - 5:
                count2 = 0

        # error_last_theta = last_theta - theta

        print 'Next KeyFrame: ', count2
        print 'Distance Error ', error_d
        print 'Distance Error x: ', error_x
        print 'Distance Error y: ', error_y
        # print 'desired_t: ', desired_t
        print 'Error theta zed: ', coment_t
        # print 'Error theta calc: ', error_t
        # print 'last_theta: ', last_theta
        print 'Theta: ', theta
        # print 'error_last_theta', error_last_theta
        print ' '
        rate.sleep()
