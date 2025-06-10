def to7(a):
    res = ''
    while a>0:
        res = str(a%7)+res
        a = a//7
    return res
i = 7**350 + 7**150

for x in range(0, 2301):
    j = i-x
    j = to7(j)
    if j.count('0')==200:
        print(x, j)
