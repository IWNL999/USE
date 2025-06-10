i = 2*216**8 + 4*36**12 + 6**15 - 1296
def to6(a):
    res = ''
    while a>0:
        res = str(a%6)+res
        a //= 6
    return res

print(to6(i).count('0'))

