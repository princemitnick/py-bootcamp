import turtle as t
import random
import colorgram



timmy = t.Turtle()
t.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]
colors = colorgram.extract('images.jpg', 6)

directions = [0, 90, 180, 270]
timmy.pensize(2)
timmy.speed("fastest")


def getcolors():
    any_color_from_colors = random.choice(colors)
    r = any_color_from_colors.rgb.r
    g = any_color_from_colors.rgb.g
    b = any_color_from_colors.rgb.b
    return [r, g, b]

'''
timmy.circle(100)
current_heading = timmy.heading()
print(current_heading)
timmy.setheading(current_heading - 10)
timmy.circle(100)
'''

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(getcolors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)


draw_spirograph(4)

screen = t.Screen()
screen.exitonclick()
