res = []
for n in range(800000, 801000):
    for i in range(2, int(n**0.5)):
        if n%i==0:
            if (i+(n//i))%10==4:
                print(n, i+(n//i))
            break
