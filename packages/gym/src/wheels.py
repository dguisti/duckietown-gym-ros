#!/usr/bin/env python3
import gym_duckietown
from gym_duckietown.simulator import Simulator
from duckietown.dtros import DTROS, NodeType

import rospy
from rospy.core import loginfo

from sensor_msgs.msg import CompressedImage
from duckietown_msgs.msg import Twist2DStamped


class GymWheelNode(DTROS):
    def __init__(self):
        super(GymWheelNode, self).__init__(
            node_name="gym_wheels", node_type=NodeType.GENERIC)

        self.wheel_sub = rospy.Subscriber(
            "/fakebot/joy_mapper_node/car_cmd", Twist2DStamped, self.callback, queue_size=1)

        self.wheel_pub = rospy.Subscriber(
            "joy_mapper/car_cmd", Twist2DStamped, queue_size=1)
        rospy.loginfo("Wheels initialized")

    def callback(self, msg):
        rospy.loginfo("Forwarding wheel data")
        self.wheel_pub(msg)

    def run(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            rospy.loginfo("Updating wheel info")
            rate.sleep()


if __name__ == '__main__':
    node = GymWheelNode()
    rospy.spin()
