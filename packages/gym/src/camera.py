#!/usr/bin/env python3
import gym_duckietown
from gym_duckietown.simulator import Simulator
from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage


import rospy
from rospy.core import loginfo


class GymCameraNode(DTROS):
    def __init__(self):
        super(GymCameraNode, self).__init__(
            node_name="gym_camera", node_type=NodeType.GENERIC)
        self.image_pub = rospy.Publisher(
            "/fakebot/camera_node/image/compressed", CompressedImage, queue_size=1)
        self.image_sub = rospy.Subscriber(
            "camera/image/compressed", CompressedImage, self.callback, queue_size=1)

    def callback(self, msg):
        rospy.loginfo("Forwarding camera info")
        self.image_pub.publish(msg)

    def run(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            rospy.loginfo("Updating camera info")
            rate.sleep()


if __name__ == '__main__':
    node = GymCameraNode()
    rospy.spin()
