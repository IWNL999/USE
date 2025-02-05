def to4(x):
    res = ''
    while x > 0:
        res = str(x%4) + res
        x = x//4
    return res
for x in range(2006, 1, -1):
    s1 = 43**56 + 113**841 - x
    s = to4(s1)
    if (s.count('2') + s.count('0'))%2==0 and (s.count('1')+s.count('3'))%2==0 and s.count('2')<=712:
        print(x, s1)
        break
# 2001
