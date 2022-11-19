from turtle import Turtle
import random


COLORS = ["blue", "red"]


class FoodManager:
    def __init__(self):
        self.speed = 5
        self.all_foods = []
        self.create_food()

    def create_food(self):
        chance_to_create_a_turtle = random.randint(1, 10)
        if chance_to_create_a_turtle != 1:
            pass
        else:
            new_food = Turtle("turtle")
            new_food.color(random.choice(COLORS))
            new_food.penup()
            new_food.setheading(180)
            y_position = random.randint(-230, 230)
            new_food.goto(300, y_position)
            self.all_foods.append(new_food)

    def move_foods(self):
        for food in self.all_foods:
            food.forward(self.speed)

    def remove(self, food):
        self.all_foods.remove(food)
        food.goto(-500, -500)

    def remove_all(self, current_foods):
        for food in current_foods:
            food.goto(-1000, -1000)

        self.all_foods = []
        self.speed = 5

    def increase_speed(self):
        self.speed += 5
