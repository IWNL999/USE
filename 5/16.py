def to2(s1):
    return bin(int(s1))[2:]  # Перевод числа в двоичную систему

count1=0
r = []

for n in range(1, 1000):
    s = to2(n)
    s+=to2(n%4)
    res = int(s, 2)
    r.append(res)
r.sort()

for i in range(len(r)-1):
    r2 = [j for j in r if r[i]<=j<=(r[i])+65]
    if len(r2)>count1:
        count1=len(r2)
print(count1)
