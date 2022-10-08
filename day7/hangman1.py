import random

words = ["romeo", "mouse", "caviar", "keyboard", "cahier"]
# word = words[random.randint(0,len(words)-1)]
word = 'caviviara'
word_tab = list(word)
print(word_tab)
blanks = ["_"] * len(word)

letter = "v"


while blanks.__contains__("_"):
    count = 0
    letter = input("letter : ")
    while count != len(word):
        if word[count] == letter:
            blanks[count] = letter
        count += 1

    print(blanks)

print("Done.")
print(blanks)
