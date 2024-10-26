def func(a, b, r, was12):
    if a > b or a == 22:
        return 0
    elif a == b and was12 == True:
        return 1
    else:
        new_was12 = was12 or (a==12)
        return (func(a+1, b, r+"1", new_was12) +
                func(a*2, b, r+"2", new_was12) +
                func(a*3, b, r+"3", new_was12))
print(func(2, 26, "", False))

def func(a, b):
    if a > b or a == 22:
        return 0
    elif a == b:
        return 1
    else:
        return (func(a+1, b) + func(a*2, b) + func(a*3, b))

print(func(2, 12)*func(12, 26))