import itertools
for x, y, z, w in itertools.product((0, 1), repeat = 4):
    f = (x and not z) or (y==z) or not w
    if not f:
        print(w, y, z, x)
