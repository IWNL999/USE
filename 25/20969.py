from fnmatch import *
mask = '*192?3*68'
for i in range(154682, 10**11, 154682):
    if fnmatch(str(i), mask):
        print(i, i//154682)
