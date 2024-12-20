from itertools import product
alp = '012345'
s = product(alp, repeat = 3)
count=0
for i in s:
    if i[0]!='0' and i[0]>=i[1]>=i[2]:
        print(i)
        count+=1
print(count)
