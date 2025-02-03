
s = open('17/177.txt').readlines()
f = [int(i) for i in s]
mini = 99999
maxi = 0

for i in f:
    if i < mini:
        mini = i
    if i > maxi:
        maxi = i

tri = [(f[i], f[i+1], f[i+2]) for i in range(len(f)-2)]
res = []

for i in tri:
    flag = 0
    flag2 = 0
    flag3 = 0
    for j in i:
        if (len(str(abs(j)))==3):
            flag +=1
        if (j%5 == mini%7):
            flag2 +=1
        if (j%7 == maxi%5):
            flag3 +=1
    if flag>0 and flag2<=1 and flag3>=2:
        res.append(i)

summ = 0
count = 0

for i in res:
    summ += sum(i)
    count+=1

print(mini)
print(maxi)
print(count)
print(summ/(count))