from itertools import *
for x, y, z, w in product((0,1), repeat = 4):
    f = (not y or x) and not z and w
    if f:
        print(w, x, y, z)