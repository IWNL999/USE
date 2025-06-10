def deli(n, m):
    return n%m==0
for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        f = (not (35<=x<=65) or not(deli(x+1, 17))) or deli(x,a)
        if not f:
            flag = 0
            break
    if flag == 1:
        print(a)