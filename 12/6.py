num = '1' + '9'*100
while '19' in num or '299' in num or '3999' in num:
    num = num.replace('19', '2', 1)
    num = num.replace('299', '3', 1)
    num = num.replace('3999', '1', 1)
print(num)
