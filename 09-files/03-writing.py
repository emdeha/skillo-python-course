# Opening a file in write mode
file = open("example.txt", "w")

# Writing data to the file
file.write("Hello, World!\n")
file.write("This is a second line.")
file.close()


# The with statement automatically closes the file when you're done
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.")

