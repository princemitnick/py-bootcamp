import random

COLOR = ["blue", "red", "green", "purple"]
from turtle import Turtle


class HaitiDepartment(Turtle):

    def __init__(self, dept_answer, xcor, ycor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(xcor, ycor)
        self.color(random.choice(COLOR))
        self.write(dept_answer, align="center", font=("Arial", 12, "normal"))

