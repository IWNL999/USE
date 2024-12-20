alp = '0123456789ABCDEFGHIJ'
res = 0
for a in alp:
    for b in alp:
        for c in alp:
            for d in alp:
                for e in alp:
                    if a!='0':
                        num = a+b+c+d+e
                        if alp.find(a) + alp.find(e)==26 and int(a, 20)%2!=int(b, 20)%2 and int(a, 20)%2==int(c, 20)%2 and int(a, 20)%2!=int(d,20)%2 and int(a, 20)%2==int(e, 20)%2:
                            res+=1
                            print(num)
print(res)

# eeee работает)

