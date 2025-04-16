from ipaddress import *
a = ip_network('143.168.72.213/255.255.255.240', 0)
for i in a:
    print(i)