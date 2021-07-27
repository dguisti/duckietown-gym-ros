#!/usr/bin/env python3

import os
import rospy
# from duckietown.dtros import DTROS, NodeType  # , TopicType
#from duckietown_msgs.msg import Twist2DStamped, BoolStamped
#from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

import numpy as np
import cv2

from time import sleep
import base64


class ColorDetector():  # DTROS):
    def __init__(self, node_name):
        rospy.init_node('color_detector', anonymous=True)
        # super(ColorDetector, self).__init__(
        #    node_name=node_name, node_type=NodeType.CONTROL)
        self.sub = rospy.Subscriber(
            "/fakebot/camera_node/image/compressed", CompressedImage, self.process_image)

    def process_image(self, data):
        arr = np.fromstring(data.data, np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        cv2.imshow('image', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    node = ColorDetector("color_detector")
    rospy.spin()
