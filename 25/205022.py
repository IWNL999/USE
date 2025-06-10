from re import *
for i in range(0, 10**10, 10980):
    if fullmatch('20[13579][13579]22[24680]*', str(i)):
        print(i, i//10980)