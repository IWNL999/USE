d = [int(i) for i in range(17, 59)]
c = [int(i) for i in range(29, 81)]
a = []
for x in range(1, 200):
    i = not(x in d) or (not((not(x in c) and not(x in a))) or (not(x in d)))
    if i==False:
        a.append(x)
print(a)