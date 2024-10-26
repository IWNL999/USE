def func(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return func(a+1, b) + func(a*3, b) + func(a+2, b)
print(func(1, 10) * func(10, 12) * func(12, 15))  