my_list = [3, 7, 1, 9, 4, 6, 8, 2, 5]


def reverse(ls):
    # return ls[::-1]
    reversed_ls = []
    for i in range(1, len(ls) + 1):
        reversed_ls.append(ls[-i])
    return reversed_ls


print(reverse(my_list))
