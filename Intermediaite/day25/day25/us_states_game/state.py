from turtle import Turtle


class State(Turtle):

    def __init__(self, answer_state, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(f"{answer_state}", align="Center", font=("Arial", 9, "normal"))

