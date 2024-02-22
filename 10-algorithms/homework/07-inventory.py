import json


def read_inventory():
    with open('inventory.json') as inventory:
        return json.load(inventory)


def find_low_quantities(inventory):
    low_quantities = {}
    for name, qty in inventory.items():
        if qty < 10:
            low_quantities[name] = qty
    return low_quantities


print(find_low_quantities(read_inventory()))
