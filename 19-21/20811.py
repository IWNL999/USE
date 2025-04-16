def f(s, h):
    if s>50:
        return h%2==0
    elif h==0:
        return 0
    else:
        m = [
            f(s+1, h-1),
            f(s+4, h-1),
            f(s*2, h-1)
        ]
        return all(m) if h%2==0 else any(m)
print([s for s in range(51) if f(s, 2)])
print([s for s in range(51) if f(s, 3)])
print([s for s in range(51) if f(s, 4)])