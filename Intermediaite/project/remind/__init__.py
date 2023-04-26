from person import Person

list_1 = [1, 2, 3, 4, 5, 6]

dict_1 = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5"
}

for key, value in dict_1.items():
    print(key, value)

person1 = Person("Jean", "Pierre")

print(person1.lastname)
