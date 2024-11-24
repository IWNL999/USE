f = open("9.txt")
count = 0
for s in f:
    a = sorted(map(int, s.split()))
    if (a[0] + a[-1]) <= (a[1]+a[2]):
        count+=1
print(count)