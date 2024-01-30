even_sum = 0

for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num

print(f"Sum of all even numbers: {even_sum}")
print(f"Sum of all numbers: {sum(range(1, 100))}")
