import random

print("Black Jack Game")

user_hands = []

computer_hands = []


def blackjack(user_score, computer_score):
    if user_score == 21 or computer_score == 21:
        return True
    else:
        return False


def checkwinner(user_score, computer_score):
    if computer_score > 21:
        print("You win!")
    elif computer_score == 21:
        print("you lose!")
    elif user_score == 21 and computer_score < 21:
        print("you win!")
    elif user_score > computer_score:
        print("you win!")
    else:
        print("you lose!")



def blackjack_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hands = [random.choice(cards), random.choice(cards)]
    computer_hands = [random.choice(cards), random.choice(cards)]

    user_score = get_user_score(user_hands)
    computer_score = get_computer_score(computer_hands)

    print(f"User hands : {user_hands}, score : {user_score}")
    print(f"computer first card : {computer_hands[0]}")

    if blackjack(user_score, computer_score):
        checkwinner(user_score, computer_score)
    else:
        pass


def get_user_score(list_computer_hands):
    score = 0
    for x in list_computer_hands:
        score += x
    return score


def get_computer_score(list_computer_hands):
    score = 0
    for x in list_computer_hands:
        score += x
    return score


def check_computer_score(list_computer_hands):
    score = get_computer_score(list_computer_hands)
    check = False
    if score < 17:
        check = True
    else:
        check = False

    return check


def check_user_over_score(list_user_hands):
    score = get_user_score(list_user_hands)
    check = False
    if score == 21:
        for x in range(0, len(list_user_hands)):
            if list_user_hands[x] == 11:
                check = True

    return check


blackjack_game()