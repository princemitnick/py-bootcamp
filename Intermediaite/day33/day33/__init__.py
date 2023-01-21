import requests

URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=URL)

# Raise Exception
response.raise_for_status()

data = response.json()

iss_position = (data['iss_position']['latitude'], data['iss_position']['longitude'])

print(iss_position)