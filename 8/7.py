from itertools import product
 
s = product('123456789ABCDEF',repeat = 6)
k = 0
for i in s:
    p = ''.join(i)
    if p.count('A')+p.count('B')+p.count('C')+p.count('D')+p.count('E')+p.count('F')<5:
        k += 1
print(k*21)# 21 способ поставить два 0 на 8 мест.