from ipaddress import *
net = ip_network('98.71.254.171/255.248.0.0', 0)
print(net[0])
for i in net:
    a = f'{i:b}'
    if a.count('1')%7==0:
        print(i)
        break