def f(a, h):
    if a > 111:
        return h%2==0
    elif h==0:
        return 0
    else:
        m = []
        if (a+1)%2==0:
            m.append(f(a+1, h-1))
        if (a+2)%2==0:
            m.append(f(a+2, h-1))
        if (a*2)%2==0:
            m.append(f(a*2, h-1))
        return all(m) if h%2==0 else any(m)
print([a for a in range(112) if f(a, 4) > f(a, 2)])