import csv

# Open the CSV file for reading
with open("people.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = reader.__next__()

    print(','.join(header))

    # Iterate through each row in the CSV file
    for row in reader:
        # Each row is a list of values
        name, age, city = row

        print(f"{name},{age},{city}")
