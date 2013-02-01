#!/usr/bin/env python
import roslib; roslib.load_manifest('smr')
import rospy
import wx
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class MyForm(wx.Frame):

    
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist)
        rospy.init_node('keyboard')
        
        wx.Frame.__init__(self, None, wx.ID_ANY, "Key Press Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        btn = wx.Button(panel, label="OK")
 
        btn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
 
    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        print keycode
        if keycode == wx.WXK_UP:
            print "you pressed up!"
            self.pub.publish(Twist(Vector3(0.2,0,0),Vector3(0,0,0)))
        elif keycode == wx.WXK_DOWN:
            print "you pressed down!"
            self.pub.publish(Twist(Vector3(-0.2,0,0),Vector3(0,0,0)))
        elif keycode == wx.WXK_LEFT:
            print "you pressed left!"
            self.pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0.3)))
        elif keycode == wx.WXK_RIGHT:
            print "you pressed right!"
            self.pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,-0.3)))
        event.Skip()
 
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm()
    frame.Show()
    app.MainLoop()