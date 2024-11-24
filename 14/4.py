s = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
alp = '0123456789ABCDEFGHIJKLMNOPQRST'
num = ''
while s>0:
    n = alp[s%25]
    num+=str(n)
    s//25
num = num[::-1]
print(num.count("0"))
