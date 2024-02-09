#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

def move():
    # Starts a new node
    rospy.init_node('circle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtlebot3/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
 
    #vel_msg.linear.x = rospy.get_param('~x')
    vel_msg.linear.x = 2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    #vel_msg.angular.z = rospy.get_param('~w')
    vel_msg.angular.z = 2

    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        t1 = t0;
        
        while(t1-t0 < 3.5):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()

        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
