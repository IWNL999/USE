from itertools import *
for x, y, z, w in product((0,1), repeat = 4):
    f = (x and not y) or (y==z) or w
    if not f:
        print(x, w, z, y)