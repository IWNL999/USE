def penis(a):
    res = ''
    while a>0:
        res = str(a%4) + res
        a = a//4
    return res

maxi = 0

for x in range(1, 3001):
    i = 4**210 + 4**110 - x
    x1 = penis(i)
    if x1.count('0')>maxi:
        maxi = x1.count('0')
        print(x, maxi)


