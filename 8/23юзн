import itertools
count=0
alp = 'ABCDEF'
for num in itertools.product(alp, repeat = 6):
    num = ''.join(num)
    if num[0]!='A' and num[0]!='E' and num[-1]!='A' and num[-1]!='E':
        count+=1
    
print(count)
