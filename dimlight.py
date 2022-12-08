from turtle import *
import colorsys

tracer(100)
bgcolor("black")
pensize(4)
h=0

for i in range(400):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.005
    color("black")
    fillcolor(c)
    begin_fill()
    rt(46.5)
    fd(i)
    circle(20,180)
    end_fill()
    circle(i,21)
    fd(100)
done()