import turtle as t
import random
import colorgram


t.colormode(255)
timmy = t.Turtle()

timmy.speed("fastest")
colors = colorgram.extract('images.jpg', 50)



def getcolors():
    any_color_from_colors = random.choice(colors)
    r = any_color_from_colors.rgb.r
    g = any_color_from_colors.rgb.g
    b = any_color_from_colors.rgb.b
    return [r, g, b]



c = 0
count = 0


while c != 10:
    timmy.goto(0, 0 + count)
    for _ in range(10):
        timmy.color(getcolors())
        timmy.pendown()
        timmy.dot(15)
        timmy.penup()
        timmy.forward(30)

    timmy.penup()
    count += 30
    c += 1

screen = t.Screen()
screen.exitonclick()