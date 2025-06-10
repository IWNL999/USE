# 1
for n in range(4, 10001):
    i = '3'+ '1'*n
    while '31' in i or '211' in i or '1111' in i:
        i = i.replace('31', '1', 1)
        i = i.replace('211', '13', 1)
        i = i.replace('1111', '2', 1)
    if sum([int(j) for j in i])==15:
        print(n)