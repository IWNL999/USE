res = []
for i in range(178965, 178983):
    deli=[]
    for j in range(2, int(i**0.5) + 1):
        if i%j==0:
            deli.append(j)
            deli.append(i//j)
    if len(deli)==2:
        res.append((i, deli))
print(res)
# 178967 937 191 1
# 178977 59659 3 1
# 178979 2011 89 1
# 178982 89491 2 1