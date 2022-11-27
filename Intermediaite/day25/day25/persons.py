import pandas

data_dict = {
    "Lastname": ["Jean Baptiste", "Pierre", "Josue", "Jean Baptiste"],
    "Firstname": ["Prince", "Polimon", "Fils", "Danie"],
    "Gender": ['m', 'm', 'm','f'],
    "Age": [23, 54, 67, 23]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("persons.csv")