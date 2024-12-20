def to3(s1):
    s1 = int(s1)
    s = ''
    while s1 > 0:
        s+=str(s1%3)
        s1 = s1//3
    s = s[::-1]
    return s
r = []
for n in range(0, 10000):
    s = to3(n)
    if (s.count('1') + s.count('2')*2)%3==0:
        s = s + '212'
    else:
        s = s + to3(2* sum(map(int, s)))
    res = int(s, 3)
    if res > 490:
        r.append(res)
print(min(r))
