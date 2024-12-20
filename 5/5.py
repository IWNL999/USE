for n in range(1, 1000):
    a = bin(n)[2:]
    b = a.count("1")
    a = a+str(b%2)
    b = a.count("1")
    a = a+str(b%2)
    r = int(a, 2)
    if r>198:
        print(r)
        break