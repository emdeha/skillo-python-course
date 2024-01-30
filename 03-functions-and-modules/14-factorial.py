# fact_5 = 5 * 4 * 3 * 2 * 1 = 120
# fact_10 = 10 * 9 * 8 * ... * 1

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial(5))
