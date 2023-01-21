import requests
from datetime import datetime

MY_LAT = 18.971188
MY_LONG = -72.285217

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

url = f"https://api.sunrise-sunset.org/json"
response = requests.get(url, params=parameters)

response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset)

sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]

print(sunrise)
print(sunset)