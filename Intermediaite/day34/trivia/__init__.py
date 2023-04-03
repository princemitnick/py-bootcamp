import requests

URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
response = requests.get(url=URL)

data = response.json()

print(data)