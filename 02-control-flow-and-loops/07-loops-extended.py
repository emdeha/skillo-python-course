employees = [
    {
        "name": "Tsvetan Tsvetanov",
        "hours": 100,
    },
    {
        "name": "Peter Petrov",
        "hours": 80,
    },
    {
        "name": "Ivan Ivanov",
        "hours": 40,
    },
]

print("Name", "|", "Hours")
print("-------------")

for employee in employees:
    print(employee["name"], employee["hours"])