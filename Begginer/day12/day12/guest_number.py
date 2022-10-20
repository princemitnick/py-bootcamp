import random

print("Guess Number Game")

exact_number = random.randint(1, 100)

print(exact_number)

guest_number = 0


count = 10
win = False


def check(c):
    global win
    while not win:
        number = int(input("Make a guest : "))
        if number == exact_number:
            print("You win")
            win = True
        elif number > exact_number:
            print("Too high")
            c = c - 1
            print(f"You have {c} remaining to guess a number")
        elif number < exact_number:
            print("Too low")
            c = c - 1
            print(f"You have {c} remaining to guess a number")
        if c == 0:
            print("You lose")
            return


def check_guest():
    global exact_number
    global count
    global win
    level = input("Type 'easy' or hard : ")

    if level == 'easy':
        check(count)
    else:
        count = count - 5
        check(count)


check_guest()
'''
if level == 'easy' and count != 0:
    while exact_number != guest_number:
        print(f"you have {count} attempts remaining to guess the number.")
        number = int(input("Make a guess : "))
        if number > exact_number:
            print("Too High")
        elif number < exact_number:
            print("Too Low, Try again")
        else:
            print("You win")
            count = 0
        count -= 1
else:
    count = 5
    while exact_number != guest_number and count != 0:
        print(f"you have {count} attempts remaining to guess the number.")
        number = int(input("Make a guess : "))
        if number > exact_number:
            print("Too High")
        elif number < exact_number:
            print("Too Low, Try again")
        else:
            print("You win")
            count = 0
        count -= 1

'''
