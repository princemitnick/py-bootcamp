print("High Lower Game")
import art
print(art.game)
from random import randint
from users import instagram
def index():
    global instagram
    return randint(0, len(instagram)-1)

print(index())

def element():
    """Get element from list"""
    global instagram
    return instagram[index()]


score = 0

playing = True

while playing:
    A = element()
    B = element()
    while A == B:
        B = element()
    print(f"Compare A : {A['name']} who is a {A['description']}")
    print(art.vs)
    print(f"B : {B['name']} who is a {B['description']}")

    choose = input("Who has more followers (A/B)? > ").lower()
    if choose == 'A':
        if A['followers'] > B['followers']:
            score += 1
            print(f"Your're right! Your current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score : {score}")
            playing = False
    elif choose == 'B':
        if B['followers'] > A['followers']:
            score += 1
            print(f"Your're right! Your current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score : {score}")
            playing = False
