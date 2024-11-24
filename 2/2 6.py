from itertools import product
for w, x, y, z in product((0, 1), repeat=4):
    a = not x or y
    b = not y or w
    c = z == (x or y)
    f = a and b or c
    if not f:
        print(y, w, z, x)