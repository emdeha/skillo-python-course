n = int(input())

for i in range(0, n + 1):
    for j in range(0, i):
        print(f"{j + 1} ", end="")
    print("")
