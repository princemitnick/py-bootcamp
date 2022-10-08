import random
import hangman_words
import hangman_art

print(hangman_art.logo)

stages = hangman_art.stages

words = hangman_words.word_list
word = words[random.randint(0, len(words) - 1)]
# word =

blanks = ["_"] * len(word)


def show_blanks():
    for x in blanks:
        print(x, end="")


attempt = len(word) + 2

show_blanks()

count_stages = len(stages)


# if "_" not in blanks
while blanks.__contains__("_") and count_stages != 0:
    count = 0
    letter = input("\nletter : ").lower()
    if len(letter) == 0 or len(letter) > 1:
        print("Only 1 letter")
    elif letter in word:
        while count != len(word):
            if word[count] == letter:
                blanks[count] = letter
            count += 1
    else:
        print("Failed, retry!")
        print(stages[count_stages - 1])
        count_stages -= 1

    show_blanks()
    attempt -= 1

if blanks.__contains__("_"):
    print("\nYou lose.")
else:
    print("\nWell Done. Bravo!")
