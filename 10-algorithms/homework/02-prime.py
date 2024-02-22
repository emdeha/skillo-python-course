import math


def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


print(is_prime(5))
print(is_prime(13))
print(is_prime(12))
