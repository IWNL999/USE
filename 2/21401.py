from itertools import *

for x, y, z, w in product((0, 1), repeat = 4):
    f = x and (not z or w) and not y
    if f:
        print(x, w, z, y)