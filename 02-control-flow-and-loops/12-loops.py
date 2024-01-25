people = [
    ("Tsvetan", 1212123030),
    ("Peter", 1313131011),
    ("Ivan", 10101010),
]
vowels = "aeiou"
vowelsTuple = ('a', 'e', 'i', 'o', 'u')

peopleDictionary = {}

for person in people:
    name = person[0]  # ("Tsvetan", 1212123030)
    ucn = person[1]

    # if name[0].lower() not in vowels:
    if not name.lower().startswith(vowelsTuple):
        continue

    peopleDictionary[name] = ucn

print(peopleDictionary)