alp = '0123456789ABC'
k=0
res=[]
for a in alp:
    for b in alp:
        for c in alp:
            num = a+b+c
            if a!='0':
                if (alp.find(b)%2==0 or (alp.find(a)%2==0 and alp.find(c)%2==0)) and k%10==7:
                    res.append(num)
                k+=1
print(len(res))
