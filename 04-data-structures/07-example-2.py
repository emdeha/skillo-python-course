n = 3

unique_numbers = {}

for i in range(0, 3):
    number = int(input())
    if unique_numbers.get(number) is None:
        unique_numbers[number] = True
    else:
        unique_numbers[number] = False

count_unique = 0
for number, is_unique in unique_numbers.items():
    if is_unique:
        count_unique += 1

print("Unique numbers:", count_unique)
