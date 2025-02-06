from re import fullmatch
for i in range(1996, 10**10, 1996):
    if fullmatch(r'1592[02468]*6[0123456789]8', str(i)):
        print(i, i//1996)