import turtle
import colorsys
tr=turtle.Turtle()
tr.tracer(100)
tr.bgcolor("black")
tr.pensize(4)
h=0

for i in range(400):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.005
    tr.color("black")
    tr.fillcolor(c)
    tr.begin_fill()
    tr.rt(46.5)
    tr.fd(i)
    tr.circle(20,180)
    tr.end_fill()
    tr.circle(i,21)
    tr.fd(100)
tr.done()