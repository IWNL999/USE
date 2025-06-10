alp = '0123456789ABC'
alp1= '13579B'
from itertools import *
c = -1
count=0
f = product(alp, repeat = 3)
for i in f:
    if i[0]!='0':
        c+=1
        if c%10==7 and not((i[0] in alp1 and i[1] in alp1) or (i[1] in alp1 and i[2] in alp1)):
            count+=1
            print(i, count)
