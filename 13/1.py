from ipaddress import *
ip_net = ip_network("112.160.0.0/255.240.0.0")
count = 0
for ip_add in ip_net:
    if bin(int(ip_add)).count("1") % 5 == 0:
        count +=1
print(count)