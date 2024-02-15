import json

catalog = {
    "catalog": [
        {
            "id": "bk101",
            "author": "Gambardella, Matthew",
            "title": "XML Developer's Guide",
            "genre": "Computer",
            "price": 44.95,
            "publish_date": "2000-10-01",
            "description": "An in-depth look at creating applications with XML."
        }
    ]
}

with open("catalog.json", "w") as catalog_file:
    json.dump(catalog, catalog_file, indent=2)

with open("catalog.json", "r") as catalog_file:
    another_dict = json.load(catalog_file)
    print("Reads json:", another_dict)
