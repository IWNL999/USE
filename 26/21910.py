f1 = open('26/26_21910.txt').readlines()
f = sorted([int(i) for i in f1], reverse=True)

res = [f[0]]
neighbors = [box for box in f if res[-1] >= box + 9]
while neighbors:
    res.append(neighbors[0])
    neighbors = [box for box in f if res[-1] >= box + 9]

print(len(res))
print(res[-1])
        

