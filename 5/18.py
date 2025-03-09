def to3(a):
    res=''
    a = int(a)
    while a > 0:
        res=str(a%3) + res
        a//=3
    return res
mini=9999
for i in range(1, 1000):
    n = to3(i)
    if i%2==0:
        n = '2' + n + to3(int(n[-1])*2)
    else:
        n = to3(int(n[0])*2) + n + '2'
    res = int(n, 3)
    if res>100 and res<mini:
        print(res)
        mini=res
