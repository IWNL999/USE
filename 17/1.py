def tosix(a):
    res = ''
    while a > 0:
        res = str(a%6) + res 
        a = a//6
    return res

def tonine(a):
    res = ''
    while a > 0:
        res = str(a%9) + res 
        a = a//9
    return res

s = open('17/1.txt').readlines()
f = [int(i) for i in s]
mini = 99999
mini2 = 99999

for i in f:
    if len(abs(tosix(i)))==4 and i < mini:
        mini = i

for i in f:
    if len(abs(tonine(i)))==3 and i < mini2:
        mini2 = i

tri = [(f[i], f[i+1], f[i+2]) for i in range(len(f)-2)]
res = []

for i in tri:
    flag = 0
    flag2 = 0
    for j in i:
        if (j%11 == mini%5):
            flag +=1
    for j in i:
        if (j%7 == mini2%13):
            flag2 +=1
    if flag==1 and flag2==1:
        res.append(i)

summ = 0
count = 0
mini3 = 9999
for i in res:
    summ += sum(i)
    count+=1
    if sum(i)<mini3:
        mini3=sum(i)

print(mini)
print(mini2)
print(mini3)
print(count)