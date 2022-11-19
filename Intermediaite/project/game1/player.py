from turtle import Turtle

GO_FORWARD = 15
GO_BACKWARD = 15
GO_UP = 5
GO_DOWN = 5
ORIGIN_COLOR = "black"
LIMIT_COLOR = "yellow"
ORIGIN_POSITION = (-280, 0)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(ORIGIN_COLOR)
        self.penup()
        self.goto(ORIGIN_POSITION)

    def go_forward(self):
        if self.xcor() > 270:
            pass
        else:
            self.forward(GO_FORWARD)

    def go_backward(self):
        if self.xcor() < -280:
            pass
        else:
            self.backward(GO_BACKWARD)

    def go_up(self):
        if self.ycor() > 270:
            pass
        else:
            current_xcor = self.xcor()
            new_ycor = self.ycor() + 15
            self.goto(current_xcor, new_ycor)

    def go_down(self):
        if self.ycor() < -270:
            pass
        else:
            current_xcor = self.xcor()
            new_ycor = self.ycor() - 15
            self.goto(current_xcor, new_ycor)

    def reset_position(self):
        self.goto(ORIGIN_POSITION)
