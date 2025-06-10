for a in range(1000):
    flag = 1
    for x in range(1000):
        for y in range(1000):
            i = (5<y) or (x>32) or (x+2*y<a)
            if not i:
                flag = 0
                break
    if flag == 1:
        print(a)