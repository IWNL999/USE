def to3(n):
    s1 = n
    s=''
    while s1>0:
        s += str(s1%3)
        s1 = s1//3
    s = s[::-1]
    return s

for n in range(1, 1000):
    s = to3(n)
    if int(s, 3)%2==0:
        s = '2' + s + to3(int(s[-1], 3)*2)
    else:
        s = to3(int(s[0], 3)*2) + s + '2'
    res = int(s, 3)
    if res>100:
        print(res)
        break
