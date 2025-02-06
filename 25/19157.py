import fnmatch
mask = '1?3*5*954'
for i in range (6437, 10**10, 6437):
    if fnmatch.fnmatch(str(i), mask):
        print(i, i//6437)