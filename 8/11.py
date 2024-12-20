from itertools import product
alp = "КОТ"
count = 0
for a in product(alp, repeat = 6):
    word = a
    if word.count('К') == 1:
        count+=1
print(count)