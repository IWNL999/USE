def to3(n):
    res = ''
    while n > 0:
        res+=str(n%3)
        n = n//3
    return res[::-1]

for n in range(1, 1000):
    s = to3(n)
    r = s
    s1 = sum([int(i) for i in s])
    if n%3==0:
        r+=s[-2]
        r+=s[-1]
    else:
        r+=to3(s1)
    if int(r, 3)>220 and int(r, 3)%2==0:
        print(int(r, 3))
        break