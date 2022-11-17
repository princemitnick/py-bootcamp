import time
from turtle import Turtle
import random


COLORS = ["blue", "red", "yellow", "black", "pink", "green"]
cars = []

class Car:

    def __init__(self):
        self.INITIAL_MOVE = 20
        self.x_pos = 0
        self.y_pos = 0
        self.cars = []
        self.create_car()

    def create_car(self):
        chance_number = random.randint(500, 1000)
        if chance_number % 5 == 0 and chance_number % 10 == 0:
            self.y_pos = random.randint(-230, 230)
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, self.y_pos)
            self.cars.append(car)
        else:
            pass

    def move(self):
        for car in self.cars:
            car.backward(self.INITIAL_MOVE)

    def increase_move(self):
        self.INITIAL_MOVE += 5