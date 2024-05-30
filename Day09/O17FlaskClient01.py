
import requests

BASE ="http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld")

# print(response)
res = response.json()

# print(res)
for k,v in res.items():
    print(k, "=>", v)
