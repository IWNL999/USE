f1 = open('17/17_21903.txt').readlines()
f = [int(i) for i in f1]
tri = [(f[i], f[i+1], f[i+2]) for i in range(len(f)-2)]
res = []
res2=[]
mini=9999
for i in f:
    if abs(i)%100==15 and i<0 and len(str(i))==4 and i<mini:
        mini=i
for i in tri:
    if (i[0]<0 and i[1]<0 and i[2]<0) or (i[0]>=0 and i[1]>=0 and i[2]>=0):
        a = min(i)*max(i)
        if a>abs(mini)**2:
            res.append(i)
            res2.append(a)
print(len(res))
print(min(res2))
