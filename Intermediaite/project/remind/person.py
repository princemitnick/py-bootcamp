# Define a class
class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Instantiate an object
person1 = Person("Alice", 30)

# Call a method on the object
