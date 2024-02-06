def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


primes_less_than_100 = {num for num in range(1, 100) if is_prime(num)}
print(primes_less_than_100)
