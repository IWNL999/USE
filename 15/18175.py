def f(x):
    return not(not(x%7==0) and (x%13==0)) or (x>a-40)
for a in range(1000):
    if all(f(x)==1 for x in range(1,1000)):
        print(a)