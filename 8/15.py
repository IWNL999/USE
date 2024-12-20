import itertools
alp = 'АПРСУ'
words = itertools.product(alp, repeat = 3)
for id, word in enumerate(words, 1):
    if word[0]=='Р':
        print(id, word)
        break