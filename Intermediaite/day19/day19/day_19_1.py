from turtle import  Turtle, Screen

timmy = Turtle()

screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.right(180)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="f", fun=move_backward)
screen.exitonclick()