from ipaddress import *
a = ip_network('158.214.121.40/255.255.255.224', 0)
for i in a:
    print(i)
    