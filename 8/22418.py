from itertools import *
alp = 'ВДЁЖИНОРЯ'
f = product(alp, repeat = 5)
c = 0
for i in f:
    c+=1
    if i.count('Р')>1 and i[0]==i[-1]:
        print(i, c)
    