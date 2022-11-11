from turtle import Turtle

STYLE = ("Arial", 14, "italic")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=STYLE, align=ALIGNMENT)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()