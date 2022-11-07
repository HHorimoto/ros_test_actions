#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String
from sensor_message_getter import SensorMessageGetter

class Listener(object):
    def __init__(self, topic='/chatter', msg_wait=1.0):
        self.topic_msg = SensorMessageGetter(topic, String, msg_wait)
    
    def spin(self):
        msg_topic = self.topic_msg.get_msg()
        if msg_topic is not None:
            rospy.loginfo(rospy.get_caller_id()+" I heard %s", msg_topic.data)
        
def main():
    script_name = os.path.basename(__file__)
    node_name = os.path.splitext(script_name)[0]
    rospy.init_node(node_name)
    
    rospy.loginfo(node_name)
    
    rate = rospy.Rate(50)
    node = Listener()
    while not rospy.is_shutdown():
        node.spin()
        rate.sleep()

if __name__ == '__main__':
    main()  