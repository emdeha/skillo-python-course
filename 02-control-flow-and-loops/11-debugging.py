digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_to_find = "5"
found = False

for digit in digits:
    if digit == number_to_find:
        found = True

if found:
    print(f"Number {number_to_find} was found in the list.")
    # print("Number", number_to_find, "was found in the list.")
    # print("Number {number_to_find} was found in the list.")
else:
    print(f"Number {number_to_find} was not found in the list.")