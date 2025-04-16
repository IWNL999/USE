from fnmatch import fnmatch
f = open('24/4.txt').readline()
f = f.replace('V', "X")
f = f.replace('X', "Z")
f = f.split('Z')
maxi = 0
for i in f:
    if i.count('A') < 9 and i.count('E') < 9 and i.count('I') < 9 and i.count('O') < 9 and i.count('U') < 9 and i.count('Y') < 9 and len(i)>maxi:
        maxi=len(i)
print(maxi)

