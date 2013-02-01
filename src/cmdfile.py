#!/usr/bin/env python
import roslib; roslib.load_manifest('smr')
import rospy
from std_msgs.msg import String
import sys

# Run the program
if __name__ == "__main__":
    rospy.init_node('cmdfile')
    pub = rospy.Publisher('/smrcl_cmd', String)
    
    if sys.argv[1]:
        for line in open(sys.argv[1], "r"):
            rospy.sleep(0.5)
            pub.publish(String(line))
            print ("Sending Cmd:" + line)