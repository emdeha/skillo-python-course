my_list = [3, 7, 1, 9, 4, 6, 8, 2, 5]


def find_max(ls):
    max_elem = 0
    for elem in ls:
        if elem > max_elem:
            max_elem = elem
    return max_elem


print(find_max(my_list))
