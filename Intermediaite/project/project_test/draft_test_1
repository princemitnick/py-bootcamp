from turtle import  Turtle, Screen

block_1 = []
block_2 = []

screen = Screen()
screen.setup(width=600, height=400)

block_1_colors = ["yellow", "green", "purple"]
block_2_colors = ["red", "blue", "black"]
block_1_positions = [50, 30, 10]
block_2_positions = [-80, -100, -120]


for turtle_block1 in range(len(block_1_colors)):
    tim_turtle = Turtle()
    tim_turtle.color(block_1_colors[turtle_block1])
    tim_turtle.penup()
    tim_turtle.goto(-290, block_1_positions[turtle_block1])
    block_1.append(tim_turtle)

for turtle_block2 in range(len(block_2_colors)):
    tim_turtle = Turtle()
    tim_turtle.color(block_2_colors[turtle_block2])
    tim_turtle.penup()
    tim_turtle.goto(-290, block_2_positions[turtle_block2])
    block_2.append(tim_turtle)

on_track = True

def reset_turtle_block1_position(turtle):
    turtle.goto(-290, 50)
    turtle.forward(10)


while on_track:
    for turtle_block1 in block_1:
        if turtle_block1.xcor() > 290:
            turtle_block1.right(180)
            turtle_block1.forward(10)
        if turtle_block1.xcor() < -290 and int(turtle_block1.heading()) == 180:
            turtle_block1.right(180)
            turtle_block1.forward(10)
        else:
            turtle_block1.forward(10)

    for turtle_block2 in block_2:
        if turtle_block2.xcor() > 290:
            turtle_block2.right(180)
            turtle_block2.forward(10)
        if turtle_block2.xcor() < -290 and int(turtle_block2.heading()) == 180:
            turtle_block2.right(180)
            turtle_block2.forward(10)
        else:
            turtle_block2.forward(10)




screen.exitonclick()