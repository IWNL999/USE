def f(a, b, h):
    if a>77 or b>77:
        return h%2==0
    elif h==0:
        return 0
    else:
        if a>b:
            m = [
                f(a+1, b, h-1),
                f(a+2, b, h-1),
                f(a+3, b, h-1),
                f(a, b*2, h-1)
            ]
        elif a<b:
            m = [
                f(a, b+1, h-1),
                f(a, b+2, h-1),
                f(a, b+3, h-1),
                f(a*2, b, h-1)
            ]
        elif a==b:
            m = [
                f(a+1, b, h-1),
                f(a+2, b, h-1),
                f(a+3, b, h-1),
                f(a, b+1, h-1),
                f(a, b+2, h-1),
                f(a, b+3, h-1)
            ]
        return all(m) if h%2==0 else any(m)
    
print([s for s in range(1, 78) if f(69, s, 4)>f(69, s, 2)])


# res = []
# for a in range(1, 78):
#     for b in range(1, 78):
#         if f(a, b, 1):
#             res.append(a+b)
# print(min(res))