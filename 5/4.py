for n in range(1, 100):
    n2 = bin(n)[2:]
    n2 += str(n2.count("1")%2)
    n2 += str(n2.count("1")%2)
    n2 = int(n2, 2)
    if n2>75:
        print(n2) 