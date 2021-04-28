import requests

link = "https://api.npoint.io/5abcca6f4e39b4955965"

res = requests.get(url=link)
data = res.json()

for y in data[0]:
    print(y)

