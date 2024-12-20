from itertools import product
for a, b, c, d in product((0,1), repeat=4):
    f = c and (a or b) and (not d or b)
    if f==1:
        print(b,c,a,d)
