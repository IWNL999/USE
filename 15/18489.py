def cif(x, y):
    return (x%10 == y%10)
for a in range(1, 1000):
    if all(not(not(cif(x, 5)) and cif(x, 4)) or (x>a-11) for x in range(1, 10000)):
        print(a)