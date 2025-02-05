def nod(n, m, k):
    deli = []
    for x in range(1, min(n, m)+1, 1):
        if n%x==0 and m%x==0:
            deli.append(x)
    if len(deli)>0:        
        return (max(deli))==k
    else:
        return 0
    
count=0

for a in range(1000):
    if all(nod(a, 420, 2)==1 or (nod(a, x, 12)==1 or not nod(110, x, 11)==1) for x in range(1, 1000)):
        count+=1
print(count)
