import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_player_1 = Paddle((350, 0))
paddle_player_2 = Paddle((-350, 0))

ball = Ball((0, 0))

scoreboard = Scoreboard()

screen.onkey(fun=paddle_player_1.go_up, key="Up")
screen.onkey(fun=paddle_player_1.go_down, key="Down")

screen.onkey(fun=paddle_player_2.go_up, key="w")
screen.onkey(fun=paddle_player_2.go_down, key="s")

screen.update()
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_player_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_player_2) < 50 and ball.xcor() \
            < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.update()
screen.exitonclick()