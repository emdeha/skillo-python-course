def count_words(string: str):
    return len(string.split(' '))


def count_each_word(string: str):
    words = {}

    for word in string.split(' '):
        if words.get(word) is None:
            words[word] = 1
        else:
            words[word] += 1

    return words


print(count_each_word("ala bala nica ala ala nica"))
