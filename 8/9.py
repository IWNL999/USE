import itertools
alp = 'АМРТ'
words = itertools.product(alp, repeat = 4)
for ind, word in enumerate(words, 1):
    if ind == 250:
        print(ind, word)