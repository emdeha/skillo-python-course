listOne = range(1, 10)  # [1, 10) -> [1, 9]

for a in listOne:
    for b in listOne:
        result = a * b
        print(f"{a} * {b} = {result}")
