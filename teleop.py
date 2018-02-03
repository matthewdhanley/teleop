#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# BUTTON ASSIGNMETS
A_BUTTON = 0
B_BUTTON = 1
X_BUTTON = 2
Y_BUTTON = 3
LB_BUTTON = 4
RB_BUTTON = 5
SELECT_BUTTON = 6
START_BUTTON = 7
POWER_BUTTON = 8
L3_BUTTON = 9
R3_BUTTON = 10

# AXES ASSIGNMENTS
LEFT_STICK_X = 0
LEFT_STICK_Y = 1
LEFT_TRIGGER = 2
RIGHT_STICK_X = 3
RIGHT_STICK_Y = 4
RIGHT_TRIGGER = 5
DPAD_X = 6
DPAD_Y = 7


def callback(data):
    cmd_vel = Twist()

    cmd_vel.angular.x = data.axes[RIGHT_STICK_X]

    cmd_vel.linear.x = data.axes[LEFT_STICK_Y]

    pub.publish(cmd_vel)


def start():
    global pub
    pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
    rospy.Subscriber("joy",Joy,callback)
    rospy.init_node('teleop')
    print "Teleop Started"
    rospy.spin()

if __name__ == '__main__':
    start()
