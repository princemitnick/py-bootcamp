'''
import turtle
import time
from turtle import  Turtle, Screen

timmy = Turtle()

turtle.shape("turtle")
timmy.color("red")



print(turtle.position())
for x in range(0, 10):
    turtle.forward(x)
    time.sleep(1)

turtle.right(90)
for x in range(0, 10):
    turtle.forward(x)
    time.sleep(1)

turtle.right(90)
for x in range(0, 10):
    turtle.forward(x)
    time.sleep(1)

turtle.right(90)
for x in range(0, 10):
    turtle.forward(x)
    time.sleep(1)



my_screen = Screen()
my_screen.exitonclick()
'''

