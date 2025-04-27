from ipaddress import *
a = ip_network('95.24.16.0/255.255.240.0', 0)
maxi = 0
for i in a:
    x = f'{i:b}'
    if x.count('1')>=maxi:
        maxi = x.count('1')
        print(i)