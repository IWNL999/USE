def tri(a):
    res = ''
    while a>0:
        res = str(a%3) + res
        a //=3
    return res

for n in range(30,100):
    n1 = tri(n)
    n2 = list(n1)
    if n%5==0:
        n1 = n1 + n2[-2] + n2[-1]
    else:
        b = tri((n%5)*2)
        n1+=b
    r = int(n1, 3)
    if r>514:
        print(r)