def f(x):
    return (x & 57 == 0) or (not(x&23 == 0) or not(x&a==0))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 100000)):
        print(a)
        break