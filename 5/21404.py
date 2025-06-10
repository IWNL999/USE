for n in range(1000):
    n1 = bin(n)[2:]
    if n1.count('1')%2==0:
        n1 = list(n1)
        n1.append('0')
        n1[0]='1'
        n1[1]='0'
    else:
        n1 = list(n1)
        n1.append('1')
        n1[0] = '1'
        n1[1] = '1'  
    n1 = ''.join(n1)      
    r = int(n1, 2)
    if r>480:
        print(n, r)
        break





