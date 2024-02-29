memoize = {}


# 0 1 1 2 3 5 8 13 21 34 ...
def fibonacci(n):
    if n <= 1:
        return n

    if memoize.get(n) is not None:
        return memoize[n]

    memoize[n] = fibonacci(n-1) + fibonacci(n-2)
    return memoize[n]


print(fibonacci(100))
