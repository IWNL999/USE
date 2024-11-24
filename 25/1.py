from fnmatch import fnmatch
#12??1*56
for x in range (317, 10**8+1, 317):
    if fnmatch(str(x), "12??1*56") and x%317==0:
        print(x, x//317)