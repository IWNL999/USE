def to3(s1):
    s1 = int(s1)
    s = ''
    while s1 > 0:
        s+=str(s1%3)
        s1 = s1//3
    s = s[::-1]
    return s
mini=9999
for n in range(1, 1000):
    s = to3(n)
    s1 = [int(i) for i in s]
    s2=s
    if n%7==0:
        s+=str(s1[-1])
        s+=str(s1[-2])
    else:
        s+=to3((n%7)*3)
    res = int(s, 3)
    if res>369 and res<mini:
        mini=res
print(mini)
