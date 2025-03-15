i = 11
k = 318
for j in range(1, 160):
    if (i*j)*k>67*2**13:
        print(j, (i*j)%8)
