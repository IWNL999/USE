for n in range(4, 1000):
    s1 = n
    s = ''
    while s1 > 0:
        s += str(s1%3)
        s1 = s1//3
    s = s[::-1]
    if s[-2]=='1' and s[-1]=='0':
        s = '2' + s
    else:
        s = '1' + s
    res = int(s, 3)
    if res>130:
        print(n)
        break