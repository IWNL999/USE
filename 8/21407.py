from itertools import *
c=0
alp1 = 'ИАЭ'
alp2 = 'ДГШ'
f = product('ДГИАШЭ', repeat = 5)
for i in f:
    if (i[0] not in alp1) and (i[4] not in alp2):
        c+=1
print(c)