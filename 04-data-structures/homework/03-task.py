import string

words = ['one', 'two', 'three']

word_lens_1 = [len(word) for word in words]
print(word_lens_1)

word_lens_2 = list(map(lambda w: len(w), words))
print(word_lens_2)

word_lens_3 = list(map(len, words))
print(word_lens_3)

word_lens_4 = []
for word in words:
    word_lens_4.append(len(word))
print(word_lens_4)

word_lens_5 = {word: len(word) for word in words}
print(word_lens_5)
