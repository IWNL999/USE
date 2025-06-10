for i in range(500001, 500102):
    deli = [1, i]
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            deli.append(j)
            deli.append(i//j)
    deli = sorted(set(deli))
    if sum(deli)%10==6:
        print(i, sum(deli), deli)