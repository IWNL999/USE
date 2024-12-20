def sumdiv(n):
    return sum(i for i in range(1, n + 1)
               if n % i == 0)

def f(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return f(a+1, b) + f(sumdiv(a), b)
print(f(2, 24))