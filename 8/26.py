import itertools
alp = '0123456789AB'
count = 0
for num in itertools.product(alp, repeat = 6):
    if num[0]!='0' and num.count('B')==1 and sum(1 for i in num if int(i, 12)%2==0)==3:
        count+=1
print(count)