from turtle import Turtle

ALIGNMENT = "center"
STYLE = ("arial", 18, "italic")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level : {self.level}", font=STYLE, align=ALIGNMENT)

    def update_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", font=STYLE, align=ALIGNMENT)