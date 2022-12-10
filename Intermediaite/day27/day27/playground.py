
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(model="Nissan")
my_car.seats = 5

#print(my_car.make)
print(my_car.model)
print(type(my_car.seats))