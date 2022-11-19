from turtle import Turtle

FONT = ("arial", 15, "normal")
ALIGNMENT = "center"
check_score = False


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = [5, 10, 15, 20, 25, 60, 70, 80, 90, 100]
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} - High Score : {self.high_score} - Level : {self.level}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.level = 1
        self.scores = [5, 10, 15, 20, 25, 60, 70, 80, 90, 100]
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def is_score(self):
        global check_score
        score_to_check = self.scores[0]
        if self.score == score_to_check:
            check_score = True
            self.scores.remove(self.scores[0])
        else:
            check_score = False

        return check_score
