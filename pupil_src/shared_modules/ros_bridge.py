'''
(*)~----------------------------------------------------------------------------------
 Pupil - eye tracking platform
 Copyright (C) 2012-2016  Pupil Labs
 Distributed under the terms of the GNU Lesser General Public License (LGPL v3.0).
 License details are in the file license.txt, distributed as part of this software.
----------------------------------------------------------------------------------~(*)
'''

from plugin import Plugin
from pyglui.cygl.utils import draw_points_norm,RGBA
from pyglui import ui

import rospy
from std_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class Ros_Bridge(Plugin):
    """
    Send gaze & world frame througt ros topic
    """
    def __init__(self, g_pool):
        super(Ros_Bridge, self).__init__(g_pool)
        rospy.init_node('pupil_bridge', anonymous=False)
        self.image_publisher = rospy.Publisher('/pupil_bridge/agent_view_raw', Image, queue_size=10)
        self.bridge = CvBridge()

    def update(self,frame,events):
        image_publisher.publish(self.bridge.cv2_to_imgmsg(frame.img, "bgr8"))


    def gl_display(self):

    def get_init_dict(self):
return {}