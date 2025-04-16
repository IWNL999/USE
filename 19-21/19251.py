def f(a, h):
    if a > 131:
        return h%2==0
    elif h==0:
        return 0
    else:
        m = [
            f(a+3, h-1),
            f(a+6, h-1),
            f(a*3, h-1),
        ]
        return all(m) if h%2==0 else any(m)
print([a for a in range(132) if f(a, 4) > f(a, 2)])