maxi=0
for n in range(4, 10001):
    i = '1' + '2'*n
    while '12' in i or '322' in i or '222' in i:
        i = i.replace('12', '2', 1)
        i = i.replace('322', '21', 1)
        i = i.replace('222', '3', 1)
    i = [int(j) for j in i]
    s = sum(i)
    if s>maxi:
        maxi=s
print(maxi)