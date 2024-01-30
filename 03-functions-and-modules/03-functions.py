def find_element(element, input_list):
    for e in input_list:
        if e == element:
            return True
    return False


my_list = [1, 2, 3, 4, 5]
element_to_find = 10

result = find_element(element_to_find, my_list)

if result:
    print(f"{element_to_find} is in the list.")
elif not result:
    print(f"{element_to_find} is not in the list.")
