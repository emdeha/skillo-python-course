def is_anagram(str_one: str, str_two: str):
    # Sorting is n * log(n)
    return sorted(str_one) == sorted(str_two)


def is_anagram_fast(str_one: str, str_two: str):
    if len(str_one) != len(str_two):
        return False

    first_anagram = {}
    for ch in str_one:
        if first_anagram.get(ch) is None:
            first_anagram[ch] = 1
        else:
            first_anagram[ch] += 1

    for ch in str_two:
        if first_anagram.get(ch) is None:
            return False
        first_anagram[ch] -= 1

    return all(map(lambda x: x == 0, first_anagram.values()))


def is_anagram_fast_wrong(str_one: str, str_two: str):
    first_anagram = {}
    for ch in str_one:
        first_anagram[ch] = True

    for ch in str_two:
        if first_anagram.get(ch) is None:
            return False

    return True


print(is_anagram_fast('bob', 'obb'))
# { 'b': 2, 'o': 1 }
# { 'b': 2, 'o': 0 }
# { 'b': 1, 'o': 0 }
# { 'b': 0, 'o': 0 }
print(is_anagram_fast('bobbb', 'obb'))
print(is_anagram_fast('anagram', 'mngaaar'))
print(is_anagram_fast('pesho', 'gosho'))
