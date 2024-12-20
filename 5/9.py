
for n in range(1, 1000):
    r = bin(n)[2:]
    r+=str(r.count('1')%2)
    r+=str(r.count('1')%2)
    if int(r, 2) > 77:
        print(n)
        break
