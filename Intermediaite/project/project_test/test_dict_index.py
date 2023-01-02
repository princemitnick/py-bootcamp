import json

# with open("./data.json") as data_file:
#     fr_words = json.load(data_file)

list_1 = [
    {
        "name": "prince",
        "age": 12
    },
    {
        "name": "junior",
        "age": 13
    },
    {
        "name": "alex",
        "age": 18
    },
]

test = {
    "name": "prince",
    "age": 12
}

test2 = {
        "name": "alex",
        "age": 18
    }

print(list_1)
for x in list_1:
    print(f"{x['name']} : {x['age']}")