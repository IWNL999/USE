maxi = 0
for n in range(4, 1000):
    i = '4'+n*'7'
    while '444' in i or '777' in i:
        if '777' in i:
            i = i.replace('777', '4', 1)
        else:
            i = i.replace('444', '7', 1)
    a = [int(j) for j in i]
    if sum(a)>maxi:
        maxi = sum(a)   
print(maxi)