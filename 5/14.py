def to8(s1):
    s1 = int(s1)
    s = ''
    while s1 > 0:
        s+=str(s1%8)
        s1 = s1//8
    s = s[::-1]
    return s

for n in range(1, 1000):
    s = to8(n)
    s1 = [int(i) for i in s]
    if n%2==0:
        s+=str(max(s1))
    else:
        s+=to8((min(s1))*2)
    res = int(s, 8)
    if res<313:
        print(n)