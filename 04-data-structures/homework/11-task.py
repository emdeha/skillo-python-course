set_one = {1, 2, 3, 4, 5}
set_two = {2, 3, 4}
set_three = {4, 5}
set_four = {2, 3, 4}

# {
#     2: False,
#     3: False,
#     4: False
# }


def is_subset(set_a, set_b):
    if len(set_a) > len(set_b):
        return False

    dict = {elem: False for elem in set_a}
    for elem in set_b:
        if dict.get(elem) is not None:
            dict[elem] = True

    return len(list(filter(lambda val: val is True, dict.values()))) == len(set_a)


print(f"set_one <= set_two {is_subset(set_one, set_two)}")
print(f"set_two <= set_one {is_subset(set_two, set_one)}")
print(f"set_three <= set_one {is_subset(set_three, set_one)}")
print(f"set_four <= set_two {is_subset(set_four, set_two)}")
