import itertools
alp = 'АОУ'
words = itertools.product(alp, repeat = 5)
for id, word in enumerate(words, 1):
    if id == 170:
        print(word)
