import itertools
for x, y, z, w in itertools.product((0, 1), repeat = 4):
    f = not((not x or y) and not w) or not(z and not(y and w))
    if f==0:
        print(y, x, w, z)