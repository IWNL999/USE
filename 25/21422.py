for i in range(1125000, 1125100):
    for j in range(2, int(i**0.5)+1):
        a = i/j
        if j%10==7 and j!=7 and i%j==0:
            print(i, j)
            break
        if a%10==7 and a!=7 and i%a==0:
            print(i, a)

''' Answer
    1125003 467
    1125006 97
    1125009 17
    1125011 3187
    1125012 177
'''