def to(a):
    res = ''
    while a>0:
        res+=str(a%6)
        a = a//6
    return res[::-1]
i = 6**260 + 6**160 + 6**60
for x in range(1, 2031):
    j = i-x
    j = to(j)
    if j.count('0')==202:
        print(x)