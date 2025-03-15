from itertools import product
alp = '2468'
res=[]
f = product(('012345678'), repeat = 5)
for i in f:
    flag = True
    if i[0]!='0' and i.count('0')==1:
        for j in range(4):
            if i[j] in alp:
                if i[j+1]=='0' or i[j-1]=='0':
                    flag = False
        if flag==True:
            res.append(''.join(i))
print(res)
print(len(res))

