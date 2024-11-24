for x in range(1, 2031):
    s = 6**260 + 6**160 + 6**60 - x
    cnt0 = 0
    while s > 0:
        if s%6 ==0:
            cnt0+=1
        s = s//6
    if cnt0 == 202:
        print(x)
        break