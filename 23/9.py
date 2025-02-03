from functools import lru_cache

@lru_cache(None)
def F1(n):
    if n < 3:
        return 2
    elif n > 2 and n % 2 == 0:  # n четное
        return 2 * F1(n - 2) - F1(n - 1) + 2
    else:  # n нечетное
        return 2 * F1(n - 1) + F1(n - 2) - 2

print(F1(170))
