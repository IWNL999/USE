from itertools import *
alp1='02468'
alp2='13579'
c=0
f = product('0123456789', repeat = 4)
for i in f:
    if i[0]!=i[1] and i[0]!=i[2] and i[0]!=i[3] and i[1]!=i[2] and i[1]!=i[3] and i[2]!=i[3] and i[0]!='0':
        flag = 1
        for j in range(3):
            if not((i[j] in alp1 and i[j+1] in alp2) or (i[j] in alp2 and i[j+1] in alp1)):
                flag = 0
        if flag==1:
            c+=1
print(c)
