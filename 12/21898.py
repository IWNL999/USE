# ПЕРВОЕ СЛЕВА
for n in range(4, 10001):
    i = '1'+'9'*n
    while '19' in i or '399' in i or '999' in i:
        i=i.replace('19', '9', 1)
        i=i.replace('399', '91', 1)
        i=i.replace('999', '3', 1)
    i = [int(j) for j in i]
    c = sum(i)
    if c==33:
        print(i,n)
