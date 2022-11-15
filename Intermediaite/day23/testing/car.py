import time
from turtle import Turtle
import random


COLORS = ["blue", "red", "yellow", "black", "pink", "green"]
cars = []


class Car:

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.cars = []
        self.create_car()

    def create_car(self):
        self.y_pos = random.randint(-230, 230)
        car = Turtle()
        car.color(random.choice(COLORS))
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, self.y_pos)
        time.sleep(2)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(30)
