import os

file_names = os.scandir("./")

idx = 0

for name in file_names:
    with open(name, "r") as file:
        print(f"Reading file {idx}")
        print(file.readline())
        idx += 1
