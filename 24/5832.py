f = open('24/24_5832.txt').readline()
maxi = 1
m = 1
for i in range(len(f)-1):
    if f[i+1]<f[i]:
        m+=1
    else:
        maxi=max(m,maxi)
        m = 1
        
print(maxi)