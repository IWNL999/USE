import itertools
alp = "АПРСУ"
words = itertools.product(alp, repeat = 4)
for id, word in enumerate(words, 1):
    if word.count('А')==0:
        print(id, word)
        break
