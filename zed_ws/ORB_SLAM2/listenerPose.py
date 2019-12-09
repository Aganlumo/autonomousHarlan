#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its

#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import PoseStamped

#This is for getting published pose from node
def callback(data, args):
    zed_pos_x_ = data.pose.position.x #data is argument for callback, pose is data attribute
    zed_pos_y_ = data.pose.position.y #position/orientation is pose attribute
    zed_theta_ = data.pose.orientation.y

    desired_x = args[51][0]
    desired_y = args[51][1]
    desired_t = args[51][2]

    error_x = zed_pos_x_ - desired_x
    error_y = zed_pos_y_ - desired_y
    error_t = zed_theta_ - desired_t

    print 'Distancia a x     : ', error_x
    print 'Distancia a y     : ', error_y
    print 'Diferencia Angulo : ', error_t
    print '   '

    # print '   '
    # print(type(data.pose.position.x))

def listener():
    #This is for opening file and comparing key poses to PoseStamped
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
                # print(type(element))
                buffer = [float(i) for i in buffer]
            buffer.pop(0)
            # print(buffer)
            # print(count)
            values.append(buffer)
        count += 1

    # zed_pose_x = rospy.get_param('zed_pose_x_')

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('ORB_SLAM2/pose', PoseStamped, callback, (values)) #(Node, msg, callback_function)

    # print zed_pose_x
    # print zed_pos_y_
    # print zed_theta_
    # print (values)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
