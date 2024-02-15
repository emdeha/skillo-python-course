import csv
import json

people = []

with open("people.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    reader.__next__()

    for row in reader:
        name, age, city = row

        people.append({
            "name": name,
            "age": age,
            "city": city
        })

with open("people.json", "w") as json_file:
    json.dump(people, json_file, indent=2)
