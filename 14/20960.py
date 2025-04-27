def penis(a):
    res = ''
    while a>0:
        res = str(a%5) + res
        a = a//5
    return res

maxi = 0

for x in range(2005, 1, -1):
    i = 5**150 + 5**98 - x
    x1 = penis(i)
    if x1.count('0')>maxi:
        maxi = x1.count('0')
        print(x, maxi)


