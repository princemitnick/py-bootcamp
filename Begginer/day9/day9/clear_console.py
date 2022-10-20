import os

countries = [
    {
        "name": "United Kingdom",
        "code": "KR",
        "capacity": 875
    },
    {
        "name": "Canada",
        "code": "CA",
        "capacity": 25
    },
    {
        "name": "Australia",
        "code": "AU",
        "capacity": 24
    },
    {
        "name": "Belgium",
        "code": "BG",
        "capacity": 30
    }
]
total = 0
max_capacity = 0
name_of_country = None

for x in range (0, len(countries)):
    if countries[x]["capacity"] > max_capacity:
        max_capacity = countries[x]["capacity"]
        name_of_country = countries[x]["name"]

print(f"Country with max capacity : {name_of_country} : {max_capacity}")
