from fnmatch import *
mask = '4*4736*1'
for i in range(0, 10**10, 7993):
    if fnmatch(str(i), mask):
        print(i, i//7993)