def f(x):
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    a = a1 <= x <= a2
    return not(not(q) or (not(not(a) and p) or not q))
r = []
d = [14.9, 15.1, 37.9, 38.1, 141.9, 142.1, 166.9, 167.1, 15, 38, 142, 167]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x)==0 for x in d):
            r+=[a2-a1]
print(min(r))
