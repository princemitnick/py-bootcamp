def turn_left():
    print()
def move():
    print()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def first_step():
    move()
    turn_left()
    move()


def second_step():
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


c = 0

while c != 6:
    first_step()
    second_step()
    c += 1

'''    
first_step()
second_step()

first_step()
second_step()


first_step()
second_step()

first_step()
second_step()


first_step()
second_step()

first_step()
second_step()

#First_Step
move()
turn_left()
move()

#Second_Step
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

#First_Step
move()
turn_left()
move()

#Second_Step
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()




move()


turn_left()
move()


turn_left()
turn_left()
turn_left()

move()
turn_left()
move()

turn_left()
move()

turn_left()
turn_left()
turn_left()
'''