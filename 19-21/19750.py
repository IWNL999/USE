def f(s, h):
    m = []
    if s<20:
        return h%2==0
    elif h==0:
        return 0
    else:
        m.append(f(s-5, h-1))
        if s%2==0:
            m.append(f(s//2, h-1))
        if s%3==0:
            m.append(f(s//3, h-1))
        if s%2!=0 and s%3!=0:
            m.append(f(s+1, h-1))
        return all(m) if h%2==0 else any(m)
print([s for s in range(20, 10000) if f(s, 4)>f(s, 2)])