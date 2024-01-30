# fact_5 = 5 * 4 * 3 * 2 * 1 = 120
#
# fact_5 = 5 * fact_4
# fact_4 = 4 * fact_3
# fact_3 = 3 * fact_2
# fact_2 = 2 * fact_1
# fact_1 = 1

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # 5 * factorial(4)
                                 # 5 * 4 * factorial(3)
                                 # 5 * 4 * 3 * factorial(2)
                                 # 5 * 4 * 3 * 2 * factorial(1)
                                 # 5 * 4 * 3 * 2 * 1


print(factorial(5))
