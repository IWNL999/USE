
def f(a, b, m, c):
    flag = False
    c=0
    if a>b or a%10==0 or m.count('11')>0 or c>15:
        c=0
        flag = False
        return 0
    elif a==32:
        flag = True
    elif a == b and flag == True:
        return 1
    else:
        c+=1
        return f(a-1, b, m+'1', 0) + f(a+2, b, m+'2', 0) + f(a*3, b, m+'3', 0)
print(f(5, 64, '0', 0))