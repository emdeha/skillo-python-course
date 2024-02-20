my_list = [3, 7, 1, 9, 4, 6, 8, 2, 5]

target = 4

found = False

# Iterate through the list to search for the target element
for num in my_list:
    if num == target:
        found = True
        break  # Exit the loop early since we found the element

if found:
    print(f"{target} was found in the list.")
else:
    print(f"{target} was not found in the list.")