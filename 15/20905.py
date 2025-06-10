def f(x):
    p = 17 <= x <= 58
    q = 29 <= x <= 80
    a = a1 <= x <= a2
    return not p or (not((q) and not a) or not p)
d = [16.9, 17.1, 17, 28.9, 29.1, 29, 57.9, 58.1, 58, 79.9, 80, 80.1]
r = []
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x)==1 for x in d):
            r.append(a2-a1)
print(min(r))

