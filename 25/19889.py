cnt=0
res=[]
for i in range (902714, 1000000):
    for j in range(15, i):
        if j%10==5 and j!=5 and cnt<6 and i not in res and i%j==0:
            print(i, j)
            cnt+=1
            res.append(i)

# 902715 15
# 902720 35
# 902725 25
# 902730 15
# 902740 225685
# 902745 15
