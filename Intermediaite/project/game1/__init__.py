import time
from turtle import Screen
from food_manager import FoodManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

food_manager = FoodManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")
screen.onkey(fun=player.go_down, key="Down")
screen.onkey(fun=player.go_forward, key="Right")
screen.onkey(fun=player.go_backward, key="Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    food_manager.create_food()
    food_manager.move_foods()

    for food in food_manager.all_foods:
        if player.distance(food) < 15 and food.pencolor() == "red":
            food_manager.remove(food)
            scoreboard.increase_score()
        elif player.distance(food) < 20 and food.pencolor() == "blue":
            current_foods = food_manager.all_foods
            food_manager.remove_all(current_foods)
            scoreboard.reset_score()
            player.reset_position()
        else:
            pass

    if scoreboard.is_score():
        scoreboard.level_up()
        food_manager.increase_speed()




screen.update()
screen.exitonclick()