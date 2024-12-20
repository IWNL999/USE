import itertools
alp = '0123456789AB'
numbers = itertools.product(alp, repeat = 5)
count = 0
for num in numbers:
    num = ''.join(num)
    if num[0]!='0' and num.count('7')==1 and (num.count('9') + num.count('A') + num.count('B'))<=3:
        count+=1
print(count)

