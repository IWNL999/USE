from fnmatch import *
for i in range(451, 10**9+1, 451):
    if fnmatch(str(i), '10?451*3'): 
        print(i, i//451)
        