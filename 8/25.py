import itertools
n=0
alp = 'АВИЙКПС'
for x in itertools.product(alp, repeat = 6):
    word = ''.join(x)
    if 'АИ' in word or 'ИА' in word or 'АА' in word or 'ИИ' in word:
        n+=1
        if word == 'КАКААА':
            print(n)
