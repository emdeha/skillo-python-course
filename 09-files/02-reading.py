with open("example.txt", 'r') as file:
    # Reading the entire file at once
    content = file.read()
    print(content)

with open("example.txt", 'r') as file:
    # Reading one line at a time
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)

with open("example.txt", 'r') as file:
    # Read the whole file line by line
    for line in file:
        print(line)

with open("example.txt", 'r') as file:
    print(file.readlines())
