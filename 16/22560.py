f = {}
for n in range(0, 80010):
    if n <180:
        f[n] = 24
    else:
        
        f[n] = f[n-12] + 6
        
print(f[80000])