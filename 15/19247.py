def f (x, y):
    return (x-3*y<a) or (y>400) or (x>56)
for a in range(1000):
    if all(f(x, y) == 1 for x in range(1, 1000) for y in range (1, 1000)):
        print(a)
        break
