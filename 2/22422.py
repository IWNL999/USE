from itertools import *
for x, y, z, w in product((0,1), repeat = 4):
    f = not((not x or w) and not y)or not (z and not(w and y))
    if not f:
        print(w, x, y, z)