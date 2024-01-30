num = int(input())
is_prime = False

if num <= 2:
    print(f"{num} is prime? True")
    exit(0)

for i in range(2, num):
    if num % i == 0:
        is_prime = True
        break

print(f"{num} is prime? {is_prime}")
