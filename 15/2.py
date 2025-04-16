for a in range(1, 10000):
    flag=1
    for x in range(1, 10000):
        i = (x&2735==0) or ((x&1234!=0) or (x&a!=0))
        if i==0:
            flag=0
    if flag == 1:
        print(a)
        break