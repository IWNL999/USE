
def f(n):
    r=''
    if n % 2 == 0:
        r = bin(n)[2:]
        r = '1' + r + '0'
    else: 
        r = bin(n)[2:]
        r = '11' + r + '11'
    return int(r, 2)

for i in range (1, 200):
    res = f(i)
    if res>52:
        print(i)