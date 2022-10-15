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
    elif user_score > 21:
        print("You lose!")
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
    # user_hands = [random.choice(cards), random.choice(cards)]
    # computer_hands = [random.choice(cards), random.choice(cards)]
    user_hands = [11, 12]
    computer_hands = [1, 3]

    user_score = get_user_score(user_hands)
    computer_score = get_computer_score(computer_hands)

    print(f"User hands : {user_hands}, score : {user_score}")
    print(f"computer first card : {computer_hands[0]}")

    get_another_card = False

    if blackjack(user_score, computer_score):
        checkwinner(user_score, computer_score)
    elif user_over_score(user_hands):

        if not has_as(user_hands):
            checkwinner(user_score, computer_score)
        else:
            change_as(user_hands)
            print(user_hands)
            new_score = get_computer_score(user_hands)
            if new_score > 21:
                checkwinner(new_score, computer_score)
                get_another_card = False
            else:
                print("You'll have another card")
                get_another_card = True


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


def user_over_score(list_user_hands):
    score = get_user_score(list_user_hands)
    check = False
    if score > 21:
        check = True

    return check


def change_as(list_user_hands):
    index = list_user_hands.index(11)
    list_user_hands[index] = 1


def has_as(list_user_hands):
    if list_user_hands.__contains__(11):
        return True
    else:
        return False


blackjack_game()


