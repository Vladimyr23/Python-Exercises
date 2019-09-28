#!/usr/bin/env python
from _markers.py import Marker
import roslib
import math
import rospy
import tf
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Point
from std_msgs.msg import Header
from sensormsgs.msg import LaserScan

LEFT=1
RIGHT=0

class Wallfollower:
    def __init__ (self):
        rospy.initnode('wallfollower')
        self.safeDistance=2
        self.following=LEFT #f o l l o w i n g w a l l on LEFT or RIGHT
        self.listener=tf.TransformListener()
        self.publisher=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.subscriber=rospy.Subscriber('/base_scan', LaserScan, self.scanReceived)
        self.m=Marker.Markers() #used f o r draw ing in r v i z

    def scanReceived (self, ls):
        a=ls.angle_min
        i=ls.angleincrement
        # i n i t i a l i s e a n g l e s f o r sc ann ing t o l e f t or r i g h t o f t h e r o b o t
        #de pen d ing on w a l l f o l l o w i n g d i r e c t i o n .
        if self.following==RIGHT:
            start=-999
            end=0
        else:
            start=0
            end=999
#s e t r ange s t o a r b i t r a r y numbers i n i t i a l l y
        rmin=9999
        amin=999
        for r in ls.ranges: #f i n d c l o s e s t p o i n t
            if (a<=end and a>=start and r<rmin):
                amin=a
                rmin=r
            a+=i
        #compute p o i n t in l a s e r frame o f r e f e r e n c e
        #and t r an s f o rm t o r o b o t frame
        x=rmin*math.cos(amin)
        y=rmin*math.sin(amin)
        ps=PointStamped(header=Header(stamp=rospy.Time(0), frame_id="/base_laser_link"), point=Point(x, y, 0))
        p=self.listener.transformPoint("/base_link", ps)
        x=p.point.x
        y=p.point.y
        mag=math.sqrt(x*x+y*y ) #u s e f u l f o r l a t e r , magn i tude o f v e c t o r
        #t a n g e n t v e c t o r
        tx=0
        ty=0
        if (self.following==RIGHT):
            tx=-y
            ty=x
        else:
            tx=y
            ty=-x

        tx/=mag
        ty/=mag
#where we s h o ul d be g o i n g
        dx=x+tx-self.safeDistance*x/mag
        dy=y+ty-self.safeDistance*y/mag
        self.m.add(dx, dy, 0, 0, 1.0, "baselink") #draw he a d ing
        theta=0
        if (dx>0 and rmin<ls.range_max): #t a n g e n t i s in f r o n t o f us
            theta=math.atan(dy/dx)
        elif (self.following==RIGHT):
            theta=-1
        else:
            theta=1
        twist=Twist()
        if (dx>0):
            twist.linear.x=dx
        twist.angular.z=theta
        self.publisher.publish(twist)
        self.m.add (0, 0, 1.0, 0, 0, "base_link") #draw o r i g i n
        self.m.draw()

robot=Wallfollower()
rospy.spin()