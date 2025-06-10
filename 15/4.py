def f(x):
    return (not(295<= x <= 400) or (5<=x<=280)) or (not(not(a1<=x<=a2)) or (375<=x<=450))
r = []
d = [y for x in (5, 280, 295, 400, 375, 450) for y in (x, x+0.1, x-0.1)]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x) for x in d):
            r+=[a2-a1]
print(min(r))