my_list = [0, 1, 3, 4, 6, 9]
my_n = 10


def find_missing_number(ls, n):
    all_numbers = {i for i in range(0, n)}
    ls_set = {elem for elem in ls}
    return all_numbers.difference(ls_set)


print(find_missing_number(my_list, my_n))