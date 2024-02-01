# Problem 4: Online Shopping Cart
#
# Create a Python program that simulates an online shopping cart using a global dictionary
# variable. Every customer has unique id as a key. Define functions to add items to the cart,
# remove items, calculate the total price, and display the contents of the cart. Allow the user to
# interact with the cart by adding and removing items.
#
# Customer
#   - id: unique key
#   - items: list[Item]
#
# Item
#   - price
#   - name
import json

customers = [
    {
        'id': 'asdf',
        'items': [
            {
                'name': 'soap',
                'price': 20,
            },
            {
                'name': 'coke',
                'price': 10,
            }
        ]
    },
    {
        'id': 'zxcv',
        'items': [
            {
                'name': 'haribo',
                'price': 5,
            }
        ]
    },
    {
        'id': 'qwer',
        'items': []
    }
]


def find_customer(customer_id):
    for customer in customers:
        if customer['id'] == customer_id:
            return customer


def add_item_to_cart(customer_id, item):
    customer = find_customer(customer_id)
    customer['items'].append(item)


def remove_item_from_cart(customer_id, item_name):
    customer = find_customer(customer_id)
    new_items = []
    for item in customer['items']:
        if item['name'] != item_name:
            new_items.append(item)
    customer['items'] = new_items


# add_item_to_cart('asdf', { 'name': 'phone', 'price': 100 })
# print(customers)
# remove_item_from_cart('asdf', 'phone')
# print(customers)


def total(customer_id):
    customer = find_customer(customer_id)
    result = 0
    for item in customer['items']:
        result += item['price']
    return result


# print(total('qwer'))


def display(customer_id):
    print(json.dumps(find_customer(customer_id), indent=4))


display('asdf')
