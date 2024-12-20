mini = 99999
for n1 in range(5, 1000):
    n = ''
    while n1 > 0:
        n += str(n1%3)
        n1= n1//3
    n = n[::-1]
    if int(n[len(n) - 1], 3) % 2 == 0:
        if n[len(n)-1] == '2':
            n = "2" + n + "11"
        else:
            n = '2' + n + '0'
    else:
        if n[0] == '1':
            n = "2" + n + "2" 
        elif n[0] == '2':
            n = "11" + n + "2" 
    res = int(n, 3)
    if res > 100 and res<mini:
        mini = res
print(mini)

# решение покруче
# def tr(x): 
#   s = ''
#   while x > 0:
#     s = str(x % 3) + s
#     x //= 3
#   return s

# for n in range(1, 100):
#   s = tr(n)
#   if n % 2 == 0:
#     s = '2' + s + tr(2*(n % 3))
#   else: 
#     s = tr(2*int(s[0])) + s + '2'
#   r = int(s, 3)
#   if r > 100:
#     print(r)