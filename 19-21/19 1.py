from sys import setrecursionlimit
setrecursionlimit(10000000)
def f(a,b,target, h = 0):
    flag = (target %2 == h%2)
    if a + b >= 150:
        return flag
    if h > target:
        return False
    m = [
        f(a+1,b,target,h+1),
        f(a+2,b,target,h+1),
        f(a+b,b,target,h+1),
        f(a,b+1,target,h+1),
        f(a,b+2,target,h+1),
        f(a,b+a,target,h+1),
        ]
    return all(m) if flag else any(m)
for s in range(1,89):
    for target in range(5):
        if f(61,s,target):
            print(s,target)  