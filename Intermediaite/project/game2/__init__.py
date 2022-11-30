import turtle

screen = turtle.Screen()
image = "./haiti-map-dep.gif"
screen.addshape(image)

tim = turtle.Turtle()
tim.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
