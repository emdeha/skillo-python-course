def even_sum_functional(ls):
    return sum(filter(even, ls))
    # return sum([num for num in ls if num % 2 == 0])


def even(num):
    return num % 2 == 0


def even_sum_procedural(ls):
    even_sum = 0
    for num in ls:
        if num % 2 == 0:
            even_sum += num
    return even_sum


print(even_sum_functional([1, 2, 3, 4]))
print(even_sum_procedural([1, 2, 3, 4]))
