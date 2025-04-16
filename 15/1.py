for a in range(100):
    flag = 1
    for x in range(1000):
        i = not (x&105==0) or (not (x&58!=0) or (x&a!=0))
        if i!=True:
            flag = 0
    if flag == 1:
        print(a)
        break