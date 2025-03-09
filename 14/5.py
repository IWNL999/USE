from string import ascii_uppercase

alphabet = "0123456789" + ascii_uppercase

for p in range(9, 37):
    for x in range(1, p):
        for y in range(p):
            for z in range(1, p):
                for w in range(1, p):
                    if int(f"{alphabet[z]}{alphabet[x]}{alphabet[y]}{alphabet[x]}5", p) + int(
                            f"{alphabet[x]}{alphabet[y]}816", p) == int(f"{alphabet[w]}{alphabet[z]}{alphabet[x]}70", p):
                        print(p, x, y, z, w)
                        print(int(f"{x}{y}{z}{w}", p))
                        break
