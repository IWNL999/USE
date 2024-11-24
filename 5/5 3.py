def f(n):
    s = str(n)
    sum1 = int(s[0]) + int(s[2]) + int(s[4])
    sum2 = int(s[1]) + int(s[3]) 
    mini = str(min(sum1, sum2))
    maxi = str(max(sum1, sum2))
    s1 = mini + maxi
    return int(s1)

for n in range (10000, 100000):
    if f(n) == 723:
        print(n)
        break
    
