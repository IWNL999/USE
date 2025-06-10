from turtle import *
pendown()
tracer(0)
right(30)
k=45
for i in range(3):
    right(150)
    forward(6*k)
    right(30)
    forward(12*k)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(2)


done()