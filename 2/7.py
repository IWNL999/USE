from itertools import product
for x, y, z, w in product((0,1), repeat = 4):
    f = not(not x or z) or (y==w) or y
    if not f:
        print(z, x, y, w)