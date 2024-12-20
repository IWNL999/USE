def d(a):
    return sum(i for i in range(1, a+1) if a%i==0)

def f(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        return f(a+1, b) + f(a+d(a), b)
print(f(2, 62))
