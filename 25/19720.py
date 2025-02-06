import re
for i in range(153, 10**8, 153):
    if re.fullmatch(r'1[13579]*2[02468]3[13579]*45', str(i)) and i%153==0:
        print(i, i//153)