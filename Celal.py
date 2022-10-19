import requests

URL = "https://anapioficeandfire.com/api/characters/583"

result = requests.get(URL)

response = result.json()

print(response)