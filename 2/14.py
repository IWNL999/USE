import itertools
for x,y,z,w in itertools.product((0,1), repeat=4):
    f = ((not x or y) or (z==x)) and (not w or z)
    print(z,w,x,y,int(f))