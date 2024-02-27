import pandas as pd

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

c = pd.read_csv(url)

print(c.head())
