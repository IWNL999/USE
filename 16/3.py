f = {}
for n in range(2200):
    if n<=4:
        f[n] = 2024
    else:
        f[n] = 2*n*f[n-1]
print((f[2134]-f[2132])/f[2132])