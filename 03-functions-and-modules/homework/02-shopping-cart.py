# Problem 4: Online Shopping Cart
#
# Create a Python program that simulates an online shopping cart using a global dictionary
# variable. Every customer has unique id as a key. Define functions to add items to the cart,
# remove items, calculate the total price, and display the contents of the cart. Allow the user to
# interact with the cart by adding and removing items.
#
# Customer
#   - id: items -> list[Item]
#
# Item
#   - price
#   - name
import json

customers = {
    'asdf': [
        {
            'name': 'soap',
            'price': 20,
        },
        {
            'name': 'coke',
            'price': 10,
        }
    ],
    'zxcv': [
        {
            'name': 'haribo',
            'price': 5,
        }
    ],
    'qwer': []
}


def add_item_to_cart(customer_id, item):
    cart = customers[customer_id]
    cart.append(item)


def remove_item_from_cart(customer_id, item_name):
    cart = customers[customer_id]
    new_items = []
    for item in cart:
        if item['name'] != item_name:
            new_items.append(item)
    customers[customer_id] = new_items


add_item_to_cart('asdf', { 'name': 'phone', 'price': 100 })
print(customers)
remove_item_from_cart('asdf', 'coke')
print(customers)


def total(customer_id):
    cart = customers[customer_id]
    result = 0
    for item in cart:
        result += item['price']
    return result


print(total('qwer'))


def display(customer_id):
    print(json.dumps(customers[customer_id], indent=4))


display('asdf')
