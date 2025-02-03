def f(a):
    a1 = [int(i) for i in str(a)]
    return max(a1)

def func(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return func(a+3, b) + func(a+f(a), b) 
print(func(10, 24) * func(24, 41))  