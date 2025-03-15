from itertools import * 
f = product(('012345678'), repeat = 6)
res=[]
res2=[]
alp = '1357'
for id, i in enumerate(f):
    if i[0]!='0':
        res.append((id, ''.join(i)))
for i in res:
    a = i[1]
    flag = True
    for j in range(0, len(a)-1):
        if str(a[j]) in alp and str(a[j+1]) in alp:
            flag = False
    if flag == True and (i[0]-59048)%10==5:
        res2.append((i[0]-59048, i[1]))
print(res[0])
print(res2[(len(res2)-1)])

k = 0
ans = ''
k1=0
for i in product('012345678',repeat = 6):
    s = ''.join(i)
    if s[0] != '0':
        k += 1
        if k % 10 == 5 and all(int(s[j]) % 2 == 0 or int(s[j + 1]) % 2 == 0 for j in range(5)):
            ans = s
            k1=k
print(k1, ans)