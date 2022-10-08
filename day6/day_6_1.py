def turn_square():
    turn_left()
    move_on()
    turn_right()
    move_on()
    turn_right()
    move_on()
    turn_right()
    move_on()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_on():
    move()
    move()


turn_square()