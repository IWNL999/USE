from re import fullmatch
for i in range(10980, 10**10, 10980):
    if fullmatch('20[13579][13579]22[02468]*', str(i)):
        print(i, i//10980)
