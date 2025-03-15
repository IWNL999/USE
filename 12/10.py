for n in range(1, 1000):
    i = '1' + n*'7'
    while '17' in i or '377' in i or '777' in i:
        if '17' in i:
            i = i.replace('17', '1', 1)
        if '377' in i:
            i = i.replace('377', '73', 1)
        if '777' in i:
            i = i.replace('777', '3', 1)  
    if i.count('3')==2:  
        print(i, n)
        break