from itertools import product
for x, y, z, w in product((0, 1), repeat = 4):
    a = (not y or x) and (z or w)
    b = (x and not w) or (y==z)
    f = not a or b
    if not f:
        print(z, w, y, x)