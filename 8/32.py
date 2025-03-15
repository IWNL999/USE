from itertools import product
k=0
res = []
alp1='02468'
alp2='13579'
for i in product(('0123456789'), repeat = 5):
    if i[0]!='0':
        k+=1
        flag = True
        for j in range(len(i)-1):
            if (i[j] in alp1 and i[j+1] in alp1) or (i[j] in alp2 and i[j+1] in alp2):
                flag=False
        if flag == True and k%15==0:
            res.append((''.join(i), k))
print(res)
