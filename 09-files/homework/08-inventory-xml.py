import xml.etree.ElementTree as ET

tree = ET.parse('inventory.xml')
root = tree.getroot()

for product in root:
    for product_property in product:
        print(product_property.text)
