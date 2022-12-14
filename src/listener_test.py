#!/usr/bin/env python

import roslaunch
import rospy
import rospkg
import sys
from std_msgs.msg import String
from sensor_message_getter import SensorMessageGetter

class Listener(object):
    def __init__(self, time_lilmit=10, topic='/chatter', msg_wait=1.0):
        self.topic_msg = SensorMessageGetter(topic, String, msg_wait)
        self.time_lilmit = time_lilmit
        self.end_time = None

    def is_time_lilmit(self):
        if self.time_lilmit is None or self.end_time is None:
            return False
        return rospy.Time.now() >= self.end_time
    
    def test_node(self):
        self.end_time = None
        if self.time_lilmit is not None:
            self.end_time = rospy.Time.now() + rospy.Duration.from_sec(self.time_lilmit)
        while self.is_time_lilmit() is False:
            msg_topic = self.topic_msg.get_msg()
            if msg_topic is not None:
                rospy.loginfo(rospy.get_caller_id()+" I heard %s", msg_topic.data)
                return True
        return False

def test_node():

    rospy.init_node('test_node', anonymous=True)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    r = rospkg.RosPack()
    p = r.get_path('ros_test_actions')
    path = p + "/launch/test.launch"
    launch = roslaunch.parent.ROSLaunchParent(uuid, [path])

    launch.start() # Launch test
    rospy.loginfo("Started")

    node = Listener()
    result = node.test_node()

    launch.shutdown()
    if result:
        rospy.loginfo("Success")
        sys.exit(0)
    else:
        rospy.loginfo("Fail")
        sys.exit(1)
    

if __name__ == '__main__':
    test_node()  