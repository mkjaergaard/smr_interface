#!/usr/bin/env python
#import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import String

rospy.init_node('smr_example')
pub = rospy.Publisher('/smrcl_cmd', String)
pub.publish(String("fwd 0.2 @v 0.2"))
rospy.sleep(0.1)
pub.publish(String("turn 90 @v 0.1"))
rospy.sleep(0.1)
pub.publish(String("fwd 0.2 @v 0.2"))
rospy.sleep(0.1)
pub.publish(String("turn 90 @v 0.1"))
rospy.sleep(0.1)
pub.publish(String("fwd 0.2 @v 0.2"))
rospy.sleep(0.1)
pub.publish(String("turn 90 @v 0.1"))
rospy.sleep(0.1)
pub.publish(String("fwd 0.2 @v 0.2"))
rospy.sleep(0.1)
pub.publish(String("turn 90 @v 0.1"))

print ("DONE")

while not rospy.is_shutdown():
    rospy.sleep(1.0)
