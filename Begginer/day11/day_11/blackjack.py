import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
your_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]


def f_computer_score(list_computer_cards):
    score = 0
    for card in list_computer_cards:
        score += card
    return score


def f_your_score(list_of_your_cards):
    score = 0
    for card in list_of_your_cards:
        score += card
    return score


def add_another_cards(list_of_your_cards):
    new_card = random.choice(cards)
    if f_your_score(list_of_your_cards) > 21 and new_card == 11:
        new_card = 1
    list_of_your_cards.append(new_card)


def check_computer_score(list_of_computer_cards):
    computer_score = 0
    for card in list_of_computer_cards:
        computer_score += card
    if computer_score > 16:
        return True
    else:
        new_computer_card = random.choice(cards)
        if computer_score > 21 and new_computer_card == 11:
            new_computer_card = 1
            list_of_computer_cards.append(new_computer_card)
        list_of_computer_cards.append(new_computer_card)
        return False
'''
if your_score(your_cards) > 21:
    print("You lose!")
if your_score == 21:
    print("You Win!")
'''




def blackjack_game():
    play_game = input("Dou you want to play a game of blackjack? (y/n) : ")
    if play_game == "y":
        your_score = f_your_score(your_cards)
        print(f"Your hands : {your_cards} your score:  {your_score}")
        print(f"Computer first card : {computer_cards[0]}")

        while your_score < 21:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass : ").lower()
            if get_another_card == "y":
                if f_computer_score(computer_cards) <= 16:
                    computer_cards.append(random.choice(cards))
                add_another_cards(your_cards)
                your_score = f_your_score(your_cards)
                print(f"Your hands : {your_cards} your score:  {your_score}")
                print(f"Computer cards : {computer_cards}")
                print(f"Computer score : {f_computer_score(computer_cards)}")
                check_winner(your_score, f_computer_score(computer_cards))
            else:
                if f_computer_score(computer_cards) <= 16:
                    computer_cards.append(random.choice(cards))
                your_score = f_your_score(your_cards)
                print(f"Your cards : {your_cards} your score:  {your_score}")
                print(f"Computer final hands : {computer_cards}")
                print(f"Computer score : {f_computer_score(computer_cards)}")
                check_winner(your_score, f_computer_score(computer_cards))


def check_winner(your_score, computer_score):
    if computer_score == 21:
        print("You lose!")
    elif your_score == 21 and computer_score < 21:
        print("You Win!")
    elif your_score > 21:
        print("You lose!")
    elif your_score == computer_score:
        print("It's a Draw!")
    elif your_score > computer_score:
        print("You Win!")
    else:
        print("You Lose!")


blackjack_game()
