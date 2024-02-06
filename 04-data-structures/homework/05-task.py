numbers = (3, 1, 2, 3)

max = -99999999
for num in numbers:
    if num > max:
        max = num
print(f"max {max}")

min = 99999
for num in numbers:
    if num < min:
        min = num
print(f"min {min}")
