from math import *
for n in range(1, 1000):
    i = ceil(log2(10+26+8164))
    v = (n*i)/8
    if 835*v>=156*1024:
        print(n)
        break