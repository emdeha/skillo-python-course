import json
import csv


# {
#   "coke": 2,
#   "bread": 1.2,
#   "lokum": 2.5
# }
def read_product_prices():
    product_prices = {}
    with open('products.json') as products:
        products_json = json.load(products)
        for product in products_json:
            product_prices[product["name"]] = product["price"]

    return product_prices


# [
#   {
#      "date": "2024-01-01",
#      "name": "coke",
#      "amount": 2
#   }, ...
# ]
def read_product_sales():
    product_sales = []
    with open('products.csv') as products:
        reader = csv.reader(products)
        reader.__next__()
        for row in reader:
            date, name, amount = row
            product_sales.append({
                "date": date,
                "name": name,
                "amount": amount
            })

    return product_sales


# {
#   "coke": 16,
#   "bread": 1.2,
#   "lokum": 5
# }
def calculate_revenue(product_sales, product_prices):
    revenue = {}
    for sales in product_sales:
        name = sales["name"]
        product_revenue = float(product_prices[name]) * float(sales["amount"])
        if revenue.get(name) is None:
            revenue[name] = product_revenue
        else:
            revenue[name] += product_revenue

    return revenue


product_prices = read_product_prices()
product_sales = read_product_sales()
revenue = calculate_revenue(product_sales, product_prices)

print(product_prices)
print(product_sales)
print(revenue)
