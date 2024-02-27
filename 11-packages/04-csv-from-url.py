import requests
import csv

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

r = requests.get(url)

rows = r.text.split('\r')
countries = csv.reader(rows)
for row in rows:
    print(row)
