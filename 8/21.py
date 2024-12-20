import itertools
alp = '0123456789ABCDEFGHIJ'
num = itertools.product(alp, repeat = 5)
count=0
for i in num:
    i=''.join(i)
    if i[0]!='0' and alp.index(i[0])%2!=alp.index(i[1])%2 and alp.index(i[1])%2!=alp.index(i[2])%2 and alp.index(i[2])%2!=alp.index(i[3])%2 and alp.index(i[3])%2!=alp.index(i[4])%2 and (alp.index(i[0]) + alp.index(i[-1]) == 26):
        count+=1
print(count)
