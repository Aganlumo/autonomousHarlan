import rospy
import math
from geometry_msgs.msg import PoseStamped
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

if __name__ == '__main__':
    count2 = 0
    values = getfile()
    rospy.init_node('listener', anonymous=True)
    while not rospy.core.is_shutdown():
        # Gabo()
        # Ctrl + C shuts program down
        print(" ")
        rospy.Subscriber('ORB_SLAM2/pose', PoseStamped, callback) #(Node, msg, callback_function)
        desired_x = values[count2][0]
        desired_y = values[count2][1]
        desired_t = values[count2][2]
        current_d = math.sqrt(zed_pos_x_*zed_pos_x_ + zed_pos_y_*zed_pos_y_)
        if last_time_stamp != time_stamp:
            delta_time = (time_stamp - last_time_stamp)*1000000000 #conversion to seconds
            # print(delta_time)
            print(' ')
            last_zed_pos_x_ = zed_pos_x_
            last_zed_pos_y_ = zed_pos_y_
            last_zed_theta_ = zed_theta_
            last_time_stamp = time_stamp
            last_d = current_d
            # print 'Actual ', time_stamp
            # print 'Last ', last_time_stamp
            speed_x = (zed_pos_x_)/delta_time
            speed_y = (zed_pos_y_)/delta_time
            # speed_t = (zed)/delta_time
            print 'Speed x: ', speed_x
            print 'Speed y: '(speed_y)
        error_x = zed_pos_x_ - desired_x #error en componente x en  m
        error_y = zed_pos_y_ - desired_y #error en componente y en m
        error_t = zed_theta_ - desired_t
        error_d = math.sqrt(error_x*error_x + error_y*error_y)
        if (error_d <= 0.1):
            count2 += 5
            if count2 > len(values) - 5:
                count2 = 0
        print count2
        print 'Distance Error ', error_d
        print 'Distance Error x: ', error_x
        print 'Distance Error y: ', error_y
        print 'Distance Error theta: ', error_t
