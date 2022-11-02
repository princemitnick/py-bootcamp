import turtle as turtle_module
import random
import colorgram


turtle_module.colormode(255)
timmy = turtle_module.Turtle()

timmy.speed("fastest")
colors = colorgram.extract('images.jpg', 50)


def random_colors():
    any_color_from_colors = random.choice(colors)
    r = any_color_from_colors.rgb.r
    g = any_color_from_colors.rgb.g
    b = any_color_from_colors.rgb.b
    return [r, g, b]

timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random_colors())
    #timmy.penup()
    timmy.forward(50)
    #timmy.pendown()
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
