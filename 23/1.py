def fn(s, h):
    if len(h) >= 3 and len(set(h[-3:])) == 1:
        return 0
    if s >= 14:
        return 1 if s == 14 else 0
    return fn(s + 1, h + '1') + fn(s * 2, h + '2')
print(fn(1, ''))


def fn(s, h,p):
    if s > h:
        return 0
    if s == h and not '111' in p and not '222' in p:
        return 1
    return fn(s + 1,h, p +'1') + fn(s*2, h,p +'2')
print(fn(1, 14,''))