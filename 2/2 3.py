from itertools import product
for x, y, z, w in product((0, 1), repeat = 4):
    f = (not(not x or w)) or (not y or z) or (not y)
    if not f:
        print(x, w, y, z)