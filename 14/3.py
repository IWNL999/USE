for x in range(0, 2031):
    s = 6**260 + 6**160+6**60 - x
    num = ''
    while s > 0:
        num+=str(s % 6)
        s = s//6
    num = num[::-1]
    if num.count("0") == 202:
        print(x)
        break
