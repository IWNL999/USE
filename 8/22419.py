from itertools import *
f = product('0123456789ABC', repeat = 7)
c=0
alp='13579B'
for i in f:
    flag = 1
    i = ''.join(i)
    if i[0]!='0':
        h = [i.count(a) for a in i]
        i = '*' + i + '*'
        if sum(h)>7:
            flag = 0
        else:
            for j in alp:
                if 'B'+ j in i or j+'B' in i:
                    flag = 0
    else:
        flag = 0
    if flag==1:
        c+=1
print(c)

