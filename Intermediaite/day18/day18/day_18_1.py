from turtle import  Turtle, Screen



def square_with_for_loop(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
def square(turtle):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

timmy = Turtle()

timmy.color("antique white")

square(timmy)

timmy.right(90)
timmy.forward(100)

square_with_for_loop(timmy)

screen = Screen()
screen.bgcolor("aquamarine3")
screen.exitonclick()


