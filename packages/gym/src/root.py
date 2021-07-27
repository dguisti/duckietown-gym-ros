#!/usr/bin/env python3
import gym_duckietown
from gym_duckietown.simulator import Simulator
from duckietown.dtros import DTROS, NodeType

import rospy
from rospy.core import loginfo

from sensor_msgs.msg import CompressedImage

import cv2

import numpy as np


class GymEnvNode(DTROS):
    def __init__(self):
        super(GymEnvNode, self).__init__(
            node_name="gym_root", node_type=NodeType.GENERIC)
        self.env = Simulator(
            seed=123,
            map_name="loop_empty",
            max_steps=500001,
            domain_rand=0,
            camera_width=640,
            camera_height=480,
            accept_start_angle_deg=4,
            full_transparency=True,
            distortion=True
        )

        self.action = [0.0, 0.0]

        self.image_pub = rospy.Publisher(
            "camera/image/compressed", CompressedImage, queue_size=1)

        self.wheel_sub = rospy.Subscriber(
            "joy_mapper/car_cmd", CompressedImage, self.callback, queue_size=1)

    def callback(self, msg):
        self.action = [0.0, 0.0]

    def run(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            rospy.loginfo("Updating environment")
            observation, reward, done, misc = self.env.step(self.action)
            #image_np = cv2.imdecode(observation, cv2.IMREAD_COLOR)
            msg = CompressedImage()
            msg.header.stamp = rospy.Time.now()
            msg.format = "jpeg"
            msg.data = np.array(cv2.imencode(
                '.jpg', observation)[1]).tostring()
            self.image_pub.publish(msg)

            if done:
                self.env.reset()
            rate.sleep()


if __name__ == '__main__':
    node = GymEnvNode()
    node.run()
    rospy.spin()
