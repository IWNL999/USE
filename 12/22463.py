from itertools import *
for n in range(4, 1001):
    alp = '>' + '1'*n + '0'*25  + '2'*25
    f = product(alp, repeat = len(alp))
