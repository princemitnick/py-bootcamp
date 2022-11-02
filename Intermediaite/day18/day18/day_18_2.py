from turtle import  *
from random import  randint, choice
color = ["blue", "red", "yellow", "purple", "black"]

timmy = Turtle()

for _ in range(10):
    timmy.pencolor(choice(color))
    timmy.circle(5 + 5)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()