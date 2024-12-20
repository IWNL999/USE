import itertools
alp = "АКРУ"
words = itertools.product(alp, repeat = 5)
for ind, word in enumerate(words, 1):
    print(ind, word)