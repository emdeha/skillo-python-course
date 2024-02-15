try:
    with open("test.txt") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("The file doesn't exist")
