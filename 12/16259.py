import itertools
summ=0
s = []
s1 = itertools.product(('4', '2'), repeat = 65)
for i in s1:
    if i.count('4')==40:
        s.append('3' + str(i) + '3')
print(s)
