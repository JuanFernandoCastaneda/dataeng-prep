import json
import requests

# File that generates a json file in which you can see the structure of the data.

url = "https://tenders.guru/api/hu/tenders"

response = requests.get(url)
print(response.json()["data"][0]["title"])

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=2)
