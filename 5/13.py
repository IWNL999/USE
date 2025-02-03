def to4(s1):
    s1 = int(s1)
    s = ''
    while s1 > 0:
        s+=str(s1%4)
        s1 = s1//4
    s = s[::-1]
    return s
mini=9999
for n in range(1, 1000):
    s = to4(n)
    if n%4==0:
        s+=s[0]
        s+=s[1]
    else:
        s+=to4((n%4)*4)
    res = int(s, 4)
    if res>291 and res<mini:
        mini=res
print(mini)