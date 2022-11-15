from turtle import  Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(0, -280)