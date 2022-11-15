import random
import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
from car import cars

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

screen.update()
screen.listen()
player = Player()
scoreboard = Scoreboard()
car = Car()

is_game_on = True

screen.onkey(fun=player.move, key="Up")

while is_game_on:
    screen.update()
    car.create_car()
    car.move()
    if player.ycor() > 280:
        scoreboard.update_score()
        player.reset_position()

    for x in car.cars:
        x.forward(10)
        if x.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False


screen.update()
screen.exitonclick()
