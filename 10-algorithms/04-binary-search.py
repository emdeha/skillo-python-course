import math

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

target = 4


def binary_search(ls):
    if len(ls) <= 2:
        for elem in ls:
            if elem == target:
                return True
        return False

    mid_element_idx = math.floor(len(ls) / 2)
    mid_element = ls[mid_element_idx]
    if target > mid_element:
        return binary_search(ls[mid_element_idx:])
    elif target < mid_element:
        return binary_search(ls[0:mid_element_idx])
    else:
        return True


found = binary_search(my_list)

if found:
    print(f"{target} was found in the list.")
else:
    print(f"{target} was not found in the list.")
