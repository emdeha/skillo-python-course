from functools import cache


# 0 1 1 2 3 5 8 13 21 34 ...
@cache
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))
