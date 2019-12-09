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

def z2n(error):
    if error < -22.6:
        gamma = 9
    elif error >= -22.6 and error < -17.6:
        gamma = 8
    elif error >= -17.6 and error < -12.6:
        gamma = 7
    elif error >= -12.6 and error < -7.6:
        gamma = 6
    elif error >= -7.6 and error < -2.6:
        gamma = 5
    elif error >= -2.6 and error < 2.5:
        gamma = 4
    elif error >= 2.5 and error < 5.1:
        gamma = 3
    elif error >= 5.1 and error < 10.0:
        gamma = 2
    elif error >= 10.0 and error < 15.1:
        gamma = 1
    elif error >= 15.1:
        gamma = 0
    return gamma

if __name__ == '__main__':
    count2 = 0
    values = getfile()
    rospy.init_node('listener', anonymous=True)
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
        error_y = desired_y - zed_pos_y_  # error en componente y en m
        # error_t = desired_t - zed_theta_ # hay que modificar para cuando el angulo se acerca 180
        error_t = (math.atan(error_x/error_y))*(180/math.pi)#error de theta con respecto a la posicion
        error_d = math.sqrt(error_x*error_x + error_y*error_y)

        if(error_t>=300):
            error_t = error_t - 360
        elif (error_t <= -300):
            error_t = error_t + 360

        kp = 1 #jugar experimentalmente
        gamma = z2n(kp*error_t)

        print 'To harlan: ', gamma
        # print 'Speed: ', speed_d
        # print 'Angular speed: ', speed_th
        pub.publish(gamma)
        pub1.publish(speed_d)
        pub2.publish(speed_th)

        if error_t <= -5:
            print 'Turn right'
        elif error_t >= 5:
            print 'Turn left'
        else:
            print 'Go straight'

        if (error_d <= 1):
            count2 += 5
            if count2 > len(values) - 5:
                count2 = 0
        print 'Next KeyFrame: ', count2
        print 'Distance Error ', error_d
        print 'Distance Error x: ', error_x
        print 'Distance Error y: ', error_y
        print 'Error theta: ', error_t
        rate.sleep()
