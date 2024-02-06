# dict = {
#     [1, 2, 3]: 'asdf',
#     [3, 3]: 'qwe'
# }


dict_impl = [None, None, None, None, None, None, None, None, 'qwe', 'asdf']


def hash_lists(ls):
    return len(ls) + sum(ls)


print(dict_impl[hash_lists([3, 3])])  # 'qwe'
print(dict_impl[hash_lists([1, 2, 3])])  # 'asdf'
