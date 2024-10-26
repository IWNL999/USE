def func(a, b):
    if a > b:
        return 0
    elif a==b:
        return 1
    else:
        return func(a+1, b) + func(a+1, b)
print(func(1, 40))