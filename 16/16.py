from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 1
    elif n>1:
        return n*(f(n-1))
    
print(int(f(2023)/f(2020)))
