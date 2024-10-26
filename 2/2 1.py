from itertools import product
for w, x, y, z in product((0, 1), repeat = 4):
    a = not (w or x or y)
    b = ((y or z) and x or y and (w or z))
    f = a and b
    if not f:
        print(w, z, y, x)