cnt = 0
for i in range(700000, 10**10):
    for j in range(17, i+1):
        if j%10==7 and i%j==0 and cnt<5:
            print(i, j)
            cnt+=1
            break
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167
