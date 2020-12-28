import requests
from fake_useragent import UserAgent

ua = UserAgent()

api_key = "TLZoG6ZcW3puGJnFgLi3fFe4OwS2Nm3uj24Kmq"

params = {
    'key': api_key,
    'location': 0
}
url = "http://proxy.tinsoftsv.com/api/changeProxy.php"

res = requests.get(url, params=params)

print(res.text)

params1 = {
    'key': api_key,
}

url1 = "http://proxy.tinsoftsv.com/api/getProxy.php"

res1 = requests.get(url1, params=params1)

if res1.json()['proxy']:
   proxy = res1.json()['proxy']  

print(proxy)

proxies = {
        "http": "http://{}".format(proxy),
        "https": "https://{}".format(proxy),
}

headers = {
    'User-Agent': ua.random
}

response = requests.get('https://httpbin.org/ip', headers = headers, proxies = proxies)

print(response.text)