from itertools import *
cnt = 0
for per in product('БОРИС', repeat=6):
    slovo = ''.join(per)
    if slovo.count('Б') == 1 and slovo.count('Р') == 1 and slovo.count('С') <= 1:
        cnt += 1
print(cnt)