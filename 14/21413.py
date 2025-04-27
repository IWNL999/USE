alp = '0123456789ABCDEFGHIJK'
for x1 in range(1, 20):
    x = alp[x1]
    i = int('82934' + x + '2', 21) + int('2924' + x + x + '7', 21) + int('67564' + x + '8', 21)
    if i%20==0:
        print(x1, i//20)