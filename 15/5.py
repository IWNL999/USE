def f(x):
    p = 14 <= x <= 100
    q = 56 <= x <= 134
    a = a1 <= x <= a2
    return not q or (not(p and not a) or not q)
d = [13.9, 14, 14.1, 55.9, 56, 56.1, 99.9, 100, 100.1, 133.9, 134, 134.1]
r = []
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x) for x in d):
            r.append(a2-a1)
print(min(r))