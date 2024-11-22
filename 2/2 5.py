from itertools import product
for w, x, y, z in product((0, 1), repeat=4):
    a = w or x or y
    b = (y or z) and x or y
    f = not a or b
    if not f:
        print(y, w, z, x)