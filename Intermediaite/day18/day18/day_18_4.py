import turtle as t
import random


timmy = t.Turtle()
t.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")


def getcolors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]

print(getcolors())
for _ in range(200):
    timmy.pencolor(getcolors())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
