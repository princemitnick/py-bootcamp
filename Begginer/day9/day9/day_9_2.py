'''
travel_log = {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}, {
    "country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
'''

import sys, os

travel_log = [
    {
        "country": "France",
        "cities_visited": [
            "Paris", "Lille", "Dijon"
        ],
        "total_visits": 12
    },

    {
        "country": "Germany",
        "cities_visited":
            [
                "Berlin", "Hamburg", "Stuttgart"
            ],
        "total_visits": 5
    }
]

print(travel_log)

def add_country(country,total_visits, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = total_visits
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)
    print(f"You've visited {country} {total_visits} times")
    print(f"You've been to ")

again = False

while not again:
    add_country("Haiti",["Port-au-Prince", "Port-de-paix"], 4)
    check  = input("Again? : ").lower()
    if check == "True":
        again = True
    else:
        os.system("clear")
        print("Ok")



#add_country("Russia", ["Moscow", "Saint Petersburg"], 2)

#print(travel_log)