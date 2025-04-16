from ipaddress import *
a = ip_network('106.184.0.0/255.248.0.0', 0)
c=0
for addr in a:
    if f'{addr:b}'.count('1')%2!=0:
        c+=1
print(c)