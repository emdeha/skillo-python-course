# 1. Ask for number of friends
number_of_friends = input("How many friends do you have? ")

# 2. Ask for each friend's name
endings = {
    1: "st",
    2: "nd",
    3: "rd",
}

for i in range(1, int(number_of_friends) + 1):
    if i not in endings:
        ending = "th"
    else:
        ending = endings[i]

    input(f"What is your {i}{ending} friend's name? ")
