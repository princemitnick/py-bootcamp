def turn_left():
    pass

def move():
    pass
def front_is_clear():
    pass

def right_is_clear():
    pass

def wall_on_right():
    pass

def wall_in_front():
    pass


def at_goal():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def first_step():
    turn_left()
    move()


def second_step():
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


c = 0
'''
while at_goal() != True:
    first_step()
    second_step()
'''

print(wall_in_front())




print(front_is_clear())





print(right_is_clear())





print(wall_on_right())





while at_goal() != True:
    if wall_in_front():
        first_step()
        second_step()
    else:
        move()
