import fnmatch 

f = open('24/24_18597.txt').readline().strip()
mask = '????.*&????.*'

f = f.replace('&&', " ")
f = f.replace('..', " ")
f = f.split(" ")

maxi = 0

for i in f:
    if i == '':
        f.remove(i)
    elif i[0]!='0' and fnmatch.fnmatch(i, mask) and len(i)>maxi and i.count('.') == 2 and i.count('&') == 1:
        maxi = len(i)
        print(i)
print('res: ', maxi)

# код не работает