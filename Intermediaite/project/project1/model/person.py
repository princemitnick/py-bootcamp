import random


class Person:

    def __init__(self, lastname, firstname, gender, dob, country):
        self.code = "A"+ str(random.randint(23434, 982343))
        self.lastname = lastname
        self.firstname = firstname,
        self.gender = gender
        self.dob = dob
        self.country = country

    def __str__(self):
        return f"{self.code} - {self.lastname} - {self.firstname} - {self.country} - {self.dob}"