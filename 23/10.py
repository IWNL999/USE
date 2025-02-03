def F2(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 3:
        result = 2
    elif n >= 3 and n % 2 == 0:
        result = F2(n - 1, cache) + F2(n - 2, cache) - n
    else:
        result = F2(n - 2, cache) - F2(n - 1, cache) + 2 * n
    cache[n] = result
    return result

result2 = F2(30)
print(result2)
