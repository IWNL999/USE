from ipaddress import *
net = ip_network('172.16.192.0/255.255.192.0', 0)
c=0
for i in net:
    a = f'{i:b}'
    if a[-1]!='0' and a.count('1')%3==0:
        print(a)
        c+=1
print(bin(192)[2:])
print(c)
