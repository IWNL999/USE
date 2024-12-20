for n in range (1, 1000):
    n = bin(n)[2:]
    a = n + str(n.count('1')%2)
    b = a + str(a.count('1')%2)
    res = int(b, 2)
    if res>93:
        print(res)
        break