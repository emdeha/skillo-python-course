import requests

url = "https://google.com"

response = requests.get(url)

if response.status_code == 200:
    print("Got successful response", response.text)
else:
    print("Got bad response", response.status_code)
