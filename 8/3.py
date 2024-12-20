a = {0: "Е", 1: "Л", 2: "М", 3: "Р", 4: "У"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                k += 1
                if a[i] == "Л":
                    print(k)  
