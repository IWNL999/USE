f = open('24/47228.txt').readline()
maxi = 0
c=1
for i in range(len(f)-1):
    a = f[i]
    b = f[i+1]
    if (a in 'CDF' and b in 'AO') or (b in 'CDF' and a in 'AO'):
        c+=1
    else:
        maxi = max(c, maxi)
        c=1
print(maxi)