from itertools import product 
alp = "АБВГД"
ar = product(alp, repeat = 5)
arl = []
for i in ar:
    arl.append(list(i))
count = 0

for j in arl:
    flag = True
    for i in range(len(j)-1):
        if j[0] == 'А' or j[i] == j[i+1]:
            flag = False
    if flag == True: count+=1
print (count)
