for a in range(0, 1000):
    flag = 1
    for x in range(0, 10000):
        f = not((x&52!=0) and (x&48==0)) or not (x&a==0)
        if not f:
            flag = 0
            break
    if flag==1:
        print(a)
        break
