def f(a, b, h):
    if a+b<=100:
        return h%2==0
    elif h==0:
        return 0
    else:
        m = [
            f(a-3, b-3, h-1),
            f(a//2, b, h-1),
            f(a, b//2, h-1)
        ]
        return all(m) if h%2==0 else any(m)
    
print([b for b in range(53, 1000) if f(48, b, 4) > f(48, b, 2)])