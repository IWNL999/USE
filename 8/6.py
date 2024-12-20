import itertools
alp = 'ЕЛМРУ'
words = itertools.product(alp, repeat = 4)
for ind, word in enumerate(words, 1):
    if word[0] == 'Л':
        print(ind, word)
        break