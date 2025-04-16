from ipaddress import *
c = 0
a = ip_network('252.67.33.87/255.248.0.0', 0)
for i in a:
    i = f'{i:b}'
    b = [j for j in i]
    if b[:16].count('1')*2<b[16:].count('1'):
        c+=1
print(c)
