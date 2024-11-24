for i in range(1, 10000):
    v1 = 1280 * 1024 * i
    v39 = v1*39
    t = v39 / 1966080
    if t <=280:
        print(2**i)
        