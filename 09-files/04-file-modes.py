# Open a source file for reading
with open("source.txt", "r") as source_file:
    # Read the content of the source file
    source_content = source_file.read()

# Open a destination file for writing
with open("/Users/tsvetan/PycharmProjects/pythonProject/09-files/destination.txt", "w") as dest_file:
    # Write the content of the source file to the destination file
    dest_file.write(source_content)

with open("example.txt", "a") as file:
    file.write("\nAnother new line\n")

with open("example.txt", "r") as file:
    print(file.readlines())

with open("new_file.txt", "x") as file:
    file.write("writing to the file")
