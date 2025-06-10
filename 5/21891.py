for n1 in range(1000):
    n = bin(n1)[2:]
    if n.count('1')%2==0:
        n = n+'0'
    else:
        n = n+'1'
    if n.count('1')%2==0:
        n = n+'0'
    else:
        n = n+'1'
    r = int(n,2)
    if r>253:
        print(n1)
        break