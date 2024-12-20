from sys import setrecursionlimit 
from functools import lru_cache
setrecursionlimit(1000000)

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        return F(n - 2) + n ** 3

def count_multiples_of_5(start, end):
    count = 0
    for n in range(start, end + 1):
        if F(n) % 5 == 0:
            count += 1
    return count

# Define the interval
start = 666666666
end = 999999999

# Count the numbers for which F(n) is a multiple of 5
result = count_multiples_of_5(start, end)
print(result)