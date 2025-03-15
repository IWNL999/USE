import itertools
count=0
for num in itertools.product((i for i in range(25)), repeat = 4):
    if num[0]!=0 and sum(1 for j in num if j%2==0)>=1 and sum(1 for j in num if j>15)>2:
        count+=1
print(count)
