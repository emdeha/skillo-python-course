people = {
    'Alice': 'alice@email.com',
    'Bob': 'bob@email.com',
    'Charlie': 'charlie@gmail.com'
}

reversed_people = {}

for name, email in people.items():
    reversed_people[email] = name

print("Reversed people:", reversed_people)

print("Reversed people with Dictionary Comprehension:", {email: name for name, email in people.items()})
