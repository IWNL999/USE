def f(a, b, h):
    if a+b>=81:
        return h%2==0
    elif h==0:
        return 0
    else:
        moves = [
            f(a+1, b, h-1),
            f(a*2, b, h-1),
            f(a, b+1, h-1),
            f(a, b*2, h-1) 
        ]
        return all(moves) if h%2==0 else any(moves)
# print([s for s in range(74) if f(7, s, 2)])
print([s for s in range(74) if f(7, s, 4)])
