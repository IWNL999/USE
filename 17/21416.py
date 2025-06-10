f1 = open('17/17_21416.txt').readlines()
f = [int(i) for i in f1]
triple = [(f[i], f[i+1], f[i+2]) for i in range(len(f)-2)]
res = []
c = 0
summ=0
for i in f:
    if i<0:
        summ+=i
for i in triple:
    if max(i)*min(i)>summ:
        c+=1
        res.append(sum(i))
        print(i)
print(c)
print(max(res))