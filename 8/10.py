import itertools
alp = 'КОТ'
count=0
words = itertools.product(alp, repeat = 6)
for word in words:
    if word.count('К')==1:
        count+=1
print(count)