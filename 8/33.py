from itertools import *
c = 0
res=[]
for i in product(('ABP'), repeat = 7):
    if i.count('A')==3 and i.count('B')==2 and i.count('P')==2:
        c+=1
        a = ''.join(i)
        res.append((a, c))
print(res)
