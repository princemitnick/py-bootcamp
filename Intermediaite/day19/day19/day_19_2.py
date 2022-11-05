from turtle import  Turtle, Screen

timmy = Turtle()
screen = Screen()

def turn():
    timmy.right(90)

def move():
    timmy.forward(10)


screen.listen()

screen.onkey(key="t", fun=turn)
screen.onkey(key="m", fun=move)
screen.exitonclick()