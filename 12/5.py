for i in range(60, 70):
    num = '1'*i
    while '111' in num:
        num = num.replace('111', '2', 1)
        num = num.replace('222', '11', 1)
    if num == '2211':
        print(i)
