for n1 in range(150, 1, -1):
    n = oct(n1)[2:]
    n2 = [int(i) for i in n]
    n3 = sum(n2)
    if n3%2==0:
        n = n[0] + n + n[0]
    else:
        n = n+n[-1]
    r = int(n, 8)
    if r<1100:
        print(r, n1)
        break
        
