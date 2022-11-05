import turtle
from turtle import  Turtle, Screen

block_1 = []
block_2 = []
block_3 = []
block_4 = []


screen = Screen()
screen.setup(width=600, height=400)

block_1_colors = ["yellow", "green", "purple"]
block_2_colors = ["red", "blue", "black"]
block_3_colors = ["aquamarine4", "brown1", "chartreuse1"]
block_4_colors = ["darkolivegreen1", "deeppink2", "goldenrod2"]
block_1_positions = [50, 30, 10]
block_2_positions = [-80, -100, -120]
block_3_positions = [-190, -170, -150]
block_4_positions = [190, 170, 150]


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
    tim_turtle.goto(290, block_2_positions[turtle_block2])
    block_2.append(tim_turtle)


for turtle_block3 in range(len(block_3_colors)):
    tim_turtle = Turtle()
    tim_turtle.penup()
    tim_turtle.right(-90)
    tim_turtle.color(block_3_colors[turtle_block3])
    tim_turtle.goto(block_3_positions[turtle_block3], -190)
    block_3.append(tim_turtle)

for turtle_block4 in range(len(block_4_colors)):
    tim_turtle = Turtle()
    tim_turtle.right(90)
    tim_turtle.penup()
    tim_turtle.color(block_4_colors[turtle_block4])
    tim_turtle.goto(block_4_positions[turtle_block4], 190)
    block_4.append(tim_turtle)

on_track = True



while on_track:
    for turtle_block1 in block_1:
        turtle_block1.pendown()
        if turtle_block1.xcor() > 290:
            turtle_block1.clear()
            turtle_block1.right(180)
            turtle_block1.forward(10)
        if turtle_block1.xcor() < -290 and int(turtle_block1.heading()) == 180:
            turtle_block1.clear()
            turtle_block1.right(180)
            turtle_block1.forward(10)
        else:
            turtle_block1.forward(10)

    for turtle_block2 in block_2:
        turtle_block2.pendown()
        if turtle_block2.xcor() > 290:
            turtle_block2.clear()
            turtle_block2.right(180)
            turtle_block2.forward(10)
        if turtle_block2.xcor() < -290 and int(turtle_block2.heading()) == 180:
            turtle_block2.clear()
            turtle_block2.right(180)
            turtle_block2.forward(10)
        else:
            turtle_block2.forward(10)

    for turtle_block3 in block_3:
        turtle_block3.pendown()
        if turtle_block3.ycor() > 190:
            turtle_block3.clear()
            turtle_block3.right(180)
            turtle_block3.forward(10)
        if turtle_block3.ycor() < -190 :
            turtle_block3.clear()
            turtle_block3.right(180)
            turtle_block3.forward(10)
        else:
            turtle_block3.forward(10)

    for turtle_block4 in block_4:
        turtle_block4.pendown()
        if turtle_block4.ycor() > 190:
            turtle_block4.clear()
            turtle_block4.right(180)
            turtle_block4.forward(10)
        if turtle_block4.ycor() < -190 :
            turtle_block4.clear()
            turtle_block4.right(180)
            turtle_block4.forward(10)
        else:
            turtle_block4.forward(10)





screen.exitonclick()