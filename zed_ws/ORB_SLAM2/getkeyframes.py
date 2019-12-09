import rospy
from std_msgs.msg import String

rfile = open("KeyFrameTrajectory_TUM_Format.txt", "r")
wfile = open("KeyFramePoses.txt", "w")
rfile = rfile.read()
rfile = rfile.split("\n")

# rfile = rfile.split("")

values = []
fileRows = len(rfile)

for item in rfile:
    buffer = []
    for element in item.split(" "):
        buffer.append(element)
        # print(type(element))
        buffer = [float(i) for i in buffer]
    if count == fileRows - 1:
        break
    buffer.pop(0)
    values.append(buffer)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Distance to %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("ORB_SLAM2/pose", String, callback)
    rospy.spin()

if ___name___ == '___main___':
    listener()
