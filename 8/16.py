import itertools
alp = 'ТИМОФЕЙ'
count = 0
words = itertools.product(alp, repeat = 5)
for word in words:
    word = ''.join(word)
    word = '0' + word + '0'  
    if word.count('Й') <= 1 and ('Й' not in word or (word[word.index('Й') - 1] != 'И' and word[word.index('Й') + 1] != 'И')) and word[1]!='Й' and word[5]!='Й':
        count+=1
        print(word)
print(count)