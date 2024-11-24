from math import *
for n in range(1, 1000):
    A = 10 + 26 + 450
    i = 9
    V = ceil((n*i)/8)
    v708 = (V*708) / 1024
    if v708 > 213:
        print(n)
        break