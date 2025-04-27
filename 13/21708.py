from ipaddress import *
a = ip_network('11.92.135.56/255.224.0.0', 0)
print(a[-2])