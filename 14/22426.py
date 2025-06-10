from sys import *
set_int_max_str_digits(9999)
def to7(a):
    res = ''
    while a>0:
        res = str(a%7)+res
        a = a//7
    return res

i = 15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809
a = to7(i)
print(a)
b = a.count('1')+a.count('3') + a.count('5')
print(len(a)-b-b)