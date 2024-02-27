import requests

url = "https://reqbin.com/echo/get/json"

r = requests.get(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
)

with open('reqbin.json', 'w') as reqbin:
    reqbin.write(r.text)
