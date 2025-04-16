f1 = open('17/217.txt').readlines()
f = [int(i) for i in f1]
pairs = [(f[i], f[i+1]) for i in range(0, len(f)-1)]
cnt=len([i for i in f if i%32==0])
c=0
maxi=0
for i in pairs:
    if (i[0]<0 or i[1]<0) and sum(i)<cnt:
        c+=1
        if sum(i)>maxi:
            maxi = sum(i)
print(c, maxi)