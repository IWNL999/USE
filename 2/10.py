import itertools

for x, y, z, w in itertools.product((0,1), repeat = 4):
    f = (not x or y) and (not y or not z) and (z or w)
    if f:
        print(w, z, y, x)