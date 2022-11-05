from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turtle_position = [0, -20, -40]
starting_position = [(0, 0), (-20, 0), (-40, 0)]
block_turtles = []

for x in range(3):
    print(x)
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    tim.goto(starting_position[x])
    block_turtles.append(tim)

screen.update()

moving = True

while moving:
    screen.update()
    time.sleep(0.1)
    for turtle in block_turtles:
        turtle.forward(20)




screen.update()

n_t = Turtle()
n_t.color("white")
n_t.shape("square")

screen.exitonclick()