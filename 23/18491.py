def f(a,b):
    if a==b:
        return 1
    elif a>b:
        return 0
    else:
        c = [i for i in str(a)]
        return f(a+3, b) + f(a+int(max(c)), b)
print(f(10, 24) * f(24, 41))