kub = [i*i*i for i in range(50)]
for n in range(3, 10000):
    s = '59' + '8'*n
    while '68' in s or '988' in s or '888' in s:
        if '68' in s:
            s = s.replace('68', '8', 1)
        if '988' in s:
            s = s.replace('988', '86', 1)
        if '888' in s:
            s = s.replace('888', '9', 1)
    s2 = [int(i) for i in s]
    if sum(s2) in kub:
        print(n)
        break