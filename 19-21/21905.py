def f(s, h):
    if s>66:
        return h%2==0
    elif h==0:
        return 0
    else:
        m = [
            f(s+1, h-1),
            f(s+4, h-1),
            f(s*3, h-1)
        ]
        return all(m) if h%2==0 else any(m)

print([s for s in range(1, 67) if f(s, 4)>f(s, 2)])