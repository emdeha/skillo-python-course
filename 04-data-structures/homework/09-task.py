words_ls = ['one', 'one', 'two', 'three']
words_str = 'one one two three'


def calc_frequency(words):
    frequency = {}  # { 'one': 2, 'two': 1, 'three': 1 }
    for word in words:
        if frequency.get(word) is not None:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


print(calc_frequency(words_ls))
print(calc_frequency(words_str.split(' ')))
