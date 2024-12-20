import itertools 
alp = 'ЕЛМУР'
words = itertools.product(alp, repeat = 4)
for ind, word in enumerate(words, 1):
    print(ind, word)
    