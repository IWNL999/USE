from turtle import *
pendown()
tracer(0)
k=3

for i in range(4):
    forward(50*k)
    left(90)
penup()
forward(50*k)
left(135)
pendown()
for i in range(2):
    forward(102*k)
    left(120)
    forward(182*k)
    left(60)
penup()
for x in range(-150,150):
    for y in range(-150,150):
        setpos(x*k,y*k)
        dot(2)

done()