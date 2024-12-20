import itertools
alp = "РУСЛАН"
words = itertools.product(alp, repeat = 5)
count=0
for word in words:
    word = ''.join(word)
    if word.count('У')<=1 and word.count('А')<=1:
        print(word)
        count+=1
print(count)