import itertools
k=0
for i in itertools.product([i for i in range(25)], repeat = 4):
    if i[0] != 0 and sum(j%2!=0 for j in i) == 1 and sum(1 for j in i if j <= 5)<=2:
        k+=1
print(k)