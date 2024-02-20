word_count = 0

with open('words.txt') as words:
    for line in words.readlines():
        word_count += len(line.split(','))

print(word_count)
