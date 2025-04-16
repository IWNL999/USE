from itertools import product
alp='2468'
count=0
res=[]
for i in product('012345678', repeat = 5):
    i = ''.join(i)
    i+='2'
    if i[0]!='0':
        if i.count('0')==1:
            j = i.find('0')
            if i[j-1] in alp and i[j+1] in alp:
                res.append(i)
print(len(res))