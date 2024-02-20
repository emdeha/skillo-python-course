import json

with open('products.json') as products_json:
    products = json.load(products_json)

    all_prices = [product["price"] for product in products]
    print("cost", sum(all_prices))
