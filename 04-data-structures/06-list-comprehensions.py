people = ["Alice", "Bob", "Anna", "Charlie", "David", "Alex", "Eve", "Frank", "Ashley", "Grace", "Bob", "David", "Frank", "Bob", "Grace", "Anna", "Ana"]

# List comprehension to filter names starting with 'A'
names_starting_with_a = [name for name in people if name.startswith("A")]

# Dictionary comprehension to map names to their lengths
name_length_dict = {name: len(name) for name in people}

# Set comprehension to keep only unique names
unique_names = {name for name in people}

# Print the results
print("Names starting with 'A':", names_starting_with_a)
names_starting_with_a.sort()
print("Sorted names starting with 'A':", names_starting_with_a)
print("Name lengths:", name_length_dict)
print("Unique names:", unique_names)
