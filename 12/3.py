for n in range(4, 10001):
    i = '4' + '2'*n
    while '42' in i or '8222' in i or '2222' in i:
        i = i.replace('42', '2', 1)
        i = i.replace('8222', '24', 1)
        i = i.replace('2222', '8', 1)
    if i.count('2')*2 + i.count('4')*4 + i.count('8')*8 == 110:
        print(n)
