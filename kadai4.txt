from swampy.TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()
print bob
        
def square(t,length):
    polygon(t,length=length,n=4)

def polyline(t, n, lenght, angle):
	for i in range(n):
		fd(t, lenght)
		lt(t, angle)

def polygon(t,length=70,n=7):
	    angle = 360.0/n
	    polyline(t,n,length,angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

def circle(t, r):
	arc(t,r,360)
	
bob.delay = 0.01
#square(bob,50)
#polygon(bob,length=100,n=5)  
#circle(t=bob,r=100)
arc(bob,80,360)


wait_for_user()
