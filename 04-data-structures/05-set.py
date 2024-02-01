# Create sets to represent club memberships
club_a = {"Alice", "Bob", "Charlie", "David"}
club_b = {"Charlie", "Eve", "Frank", "Alice"}

# Add a new member to club A
club_a.add("Grace")

# Remove a member from club B
club_b.discard("Frank")

# Find members who belong to both clubs
common_members = club_a.intersection(club_b)

# Find members who are exclusive to each club
exclusive_to_a = club_a.difference(club_b)
exclusive_to_b = club_b.difference(club_a)

# Print the results
print("Club A Members:", club_a)
print("Club B Members:", club_b)
print("Common Members:", common_members)
print("Exclusive to Club A:", exclusive_to_a)
print("Exclusive to Club B:", exclusive_to_b)
print("Popping an element:", club_a.pop())
