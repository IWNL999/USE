import itertools

for a ,b, c, d in itertools.product((0,1), repeat = 4):
    f = (not a or b) and (not b or not c) and (c or d)
    if f==1:
        print(d, c, b, a)