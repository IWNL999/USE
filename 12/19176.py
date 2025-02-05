s = '*'*200
cnt=0
while '****' in s or '???' in s:
    if '****' in s:   
        s = s.replace('****', '???', 1)
        cnt+=3
    s = s.replace('??', '*', 1)
print(cnt, s)