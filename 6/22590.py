from turtle import *
pendown()
tracer(0)
k=5
for i in range(3):
    forward(10*k)
    right(90)
    forward(15*k)
    right(90)
penup()
forward(4*k)
right(90)
forward(7)
left(90)
pendown()
for i in range(2):
    forward(80*k)
    right(90)
    forward(60*k)
    right(90)
penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4)
done()
print(10+14*4+60*80)