# 1. Task

a = 10
b = 12

print("Sum:", a + b)
print("Difference:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 2. Task

# First approach

firstPIN = "1212121010"
firstName = "Ivan Ivanov"

secondPIN = "1313131010"
secondName = "Peter Petrov"

# Second approach

firstPerson = ("1212121010", "Ivan Ivanov")
secondPerson = ("1313131010", "Peter Petrov")
thirdPerson = ("1414141010", "Georgi Gerogiev")
fourthPerson = ("1515151010", "Mihail Mihailov")
fifthPerson = ("1616161010", "Tsvetan Tsvetanov")

personDictionary = {
    firstPerson[1]: firstPerson[0]
}

print("people", personDictionary)

# Third approach

# Tuple with names and PINs (ЕГН)
tupleNames = ("Ivan Ivanov", "Georgi Georgiev", "Dimitar Dimitrov", "Atanas Atanasov", "Elena Petrova")
tuplePins = ("8301011734", "8502273899", "8604116468", "9012247144", "9807179145")

# GET names which first name starts with a vowel
dictionary = {
    tupleNames[0]: tuplePins[0],
    tupleNames[3]: tuplePins[3],
    tupleNames[4]: tuplePins[4]
}

print(dictionary)

# 3. Task

x = True
y = True

print("x or y", x or y)