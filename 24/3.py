f = open("24/24_18285.txt").readline().strip().replace('*', '+')

while '++' in f or '+0' in f:
    f = f.replace('++', "+ +").replace('+0', ' +')
m=0
for sub in f.split():
    sub = sub.strip('+')
    if '+' in sub:
        m = max(m, len(sub.split('+')))
print(m)
