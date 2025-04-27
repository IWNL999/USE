def f(a, h):
    if a<14:
        return h%2==0
    elif h==0:  
        return 0
    else:
        m=[
            f(a-2, h-1),
            f(a*2//3, h-1)
        ]
        return all(m) if h%2==0 else any(m)
# print([s for s in range(14, 150) if f(s, 2)])
# print([s for s in range(14, 150) if f(s, 3)>f(s, 1)])
print([s for s in range(14, 150) if f(s, 4)>f(s, 2)])