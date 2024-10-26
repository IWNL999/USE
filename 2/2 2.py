from itertools import product
for x, y, z in product((0, 1), repeat = 3):
    a = (x==z)
    b = (not x or (y and z))
    f = a or b
    if not f:
        print(y, z, x)

