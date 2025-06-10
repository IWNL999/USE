from itertools import *
c = 0
alp = 'АБДЕОП'
f = product(alp, repeat = 6)
for i in f:
    c+=1
    if i[0]=='О' and i.count(i[0])==1 and i.count(i[1])==1 and i.count(i[2])==1 and i.count(i[3])==1 and i.count(i[4])==1 and i.count(i[5])==1:
        print(i, c)

# 38306