num = 10
ls_one = [1, 2, 3, 5, 5, 1, 3, 7]
ls_two = [1, 2, 3, 4]


def two_sum(ls):
    for i in range(0, len(ls)):
        for j in range(0, len(ls)):
            if i == j:
                continue

            if ls[i] + ls[j] == num:
                return True

    return False


def two_sum_fast(ls):
    two_sum_dict = {}
    for i in range(0, len(ls)):
        two_sum_dict[num - ls[i]] = i

    for i in range(0, len(ls)):
        val = two_sum_dict.get(ls[i])
        if val is not None and val != i:
            return True

    return False


print(two_sum_fast(ls_one))
print(two_sum_fast(ls_two))
