import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_one = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title=f"Make your bet ", prompt=f"Which turtle will win the race? {colors} Enter a color : ")
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for turtle_index in range(len(colors)):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(-230, y_positions[turtle_index])
    all_turtles.append(timmy)

if user_bet:
    is_race_one = True

while is_race_one:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_one = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win! The {winning_color} turtle is the winner.")
            else:
                print(f"you lose! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.listen()

screen.exitonclick()
