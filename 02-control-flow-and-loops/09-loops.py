letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
digits = ['1', '2', '3', '4', '5', '6', '7', '8']

# nested for loops to generate all combinations
for letter in letters:  # A, B
    for digit in digits:  # 1, 2
        combination = letter + digit  # A1, A2, A3, ..., B1, B2
        print(combination)
