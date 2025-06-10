from turtle import *
pendown()
tracer(0)
k=30
right(90)
for i in range(4):
    right(45)
    forward(11*k)
    right(45)

penup()

for x in range(-100, 10):
    for y in range(-100, 10):
        setpos(x*k,y*k)
        dot(4)

done()

