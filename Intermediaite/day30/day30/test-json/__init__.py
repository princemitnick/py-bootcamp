import json
import random

#
#
persons = {
    1: {
        "lastname": "Jean Baptiste",
        "firstname": "Prince Stanley"
    },
    2: {
        "lastname": "Jean Baptiste",
        "firstname": "Witaker"
    },
    3: {
        "lastname": "Pierre",
        "firstname": "Noel"
    },
}
#
with open("data.json", "w") as data:
     json.dump(persons, data, indent=4)

with open("data.json", "r") as data_to_read:
    persons_from_file = json.load(data_to_read)

id_list = []

for (keys, values) in persons_from_file.items():
    id_list.append(keys)

with open("data.json", "w") as data_to_write:
    lastname = input("Lastname : ")
    firstname = input("Firstname : ")
    person_id = random.randint(4, 100)
    person = {
        person_id: {
            "lastname": lastname,
            "firstname": firstname
        }
    }
    persons_from_file.update(person)
    json.dump(persons_from_file, data_to_write, indent=4)

