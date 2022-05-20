#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def sound_publisher():
    rospy.init_node('soundtest_pub', anonymous=True)
    pub = rospy.Publisher('soundtest_topic', String, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Hello world! How are you doing today?"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        sound_publisher()
    except rospy.ROSInterruptException:
        pass