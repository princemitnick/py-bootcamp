import random

person_dict = {
    "nom": "Prince",
    "prenom": "Stanley"
}

list_of_person = [1, 2, 4, 5, 6]

# new_dict = {
#     item + 2: item for item in list_of_person
# }

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_score = {item: random.randint(20, 100) for item in names}

print(student_score)

passed_students = { key: value for (key, value) in student_score.items() if value >= 60}

print(passed_students)