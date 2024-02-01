contacts = {}

contacts["Alice"] = "alice@example.com"
contacts["Bob"] = "bob@example.com"
contacts["Charlie"] = "charlie@example.com"

print("Email for Alice:", contacts["Alice"])
print("Email for Bob:", contacts["Bob"])

contacts["Bob"] = "new_bob@example.com"

del contacts["Charlie"]

print("\nContact List:")
for name, email in contacts.items():
    print(f"{name}: {email}")

print(f"\nAll Contact Names: {contacts.keys()}")
print(f"\nAll Contact Emails: {contacts.values()}")
print(f"\nNon-existing Contact: {contacts.get('Delta', 'no_such@email.com')}")
print(f"\nExisting Contact: {contacts.get('Alice', 'no_such@email.com')}")

print(f"\nRemoving Contact: {contacts.pop('Alice')}")
print(f"\nContacts: {contacts}")

print(f"\nRemoving Non-existing Contact: {contacts.pop('Delta', 'no_such@email.com')}")

new_contacts = { 'Omega': 'omega@email.com' }
contacts.update(new_contacts)
print(f"\nMerged Contacts: {contacts}")

contacts.clear()
print(f"\nContacts: {contacts}")

contacts = { 'Alice': 'alice', 'Bob': 'bob' }

list_contacts = ['Alice', 'Bob', 'Charlie']
for contact in list_contacts:
    if contact == 'Charlie':
        print(contact)

print(list_contacts[2])


def simple_hash(s):
    hash_code = 0
    for char in s:
        # ord() returns the ASCII value of a character
        hash_code += ord(char)
    return hash_code
