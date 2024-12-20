mini = 9999
for n in range(0, 10000):
    n = bin(n)[2:]
    if len(n)%2==0:
        n = n + '1'
    else:
        n = '1' + n + '0'
    r = int(n, 2)
    if r > 666 and r<mini:
        mini = r
        
print(mini)