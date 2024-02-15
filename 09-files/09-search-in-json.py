import json

with open("catalog.json", "r") as catalog_file:
    my_catalog = json.load(catalog_file)


def search_by_title(title, catalog):
    for book in catalog["catalog"]:
        if book["title"] == title:
            return book
    return None


print(search_by_title("No such book", my_catalog))
