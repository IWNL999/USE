import fnmatch
mask = '*45?49*24'
for i in range(12602, 10**10+1, 12602):
    if fnmatch.fnmatch(str(i), mask) and i%12602==0:
        print(i, i//12602)