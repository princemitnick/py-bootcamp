import json
import random

import pandas

data = pandas.read_csv("../flashy/data/french_words.csv")

data_to_dict = data.to_dict()

print(data)
print(data_to_dict)

with open("../flashy/data/data.json", "w") as data_file:
    json.dump(data_to_dict, data_file, indent=4)

with open("../flashy/data/data_2.json", "w") as data_file:
    data_to_dict_records = data.to_dict(orient="records")
    json.dump(data_to_dict_records, data_file, indent=4)

win = True
while True:
    index = random.randint(0, len(data_to_dict_records))
    dict_to_guess = data_to_dict_records[index]
    fr_word = dict_to_guess['french']
    en_word = dict_to_guess['english']
    automatic_answer = (en_word, data_to_dict_records[random.randint(0, len(data_to_dict_records))]['english'])

    print(fr_word)
    # print(en_word)
    # print(automatic_answer)
    which_word = automatic_answer[random.randint(0, 1)]
    guess_word = input(f"Is English word for {fr_word} = {which_word} : (Y/N)").lower()

    if guess_word == 'y' and en_word == which_word:
        win = True
    elif guess_word == 'y' and en_word != which_word:
        win = False
    elif guess_word == 'n' and en_word == which_word:
        win = False
    elif guess_word == 'n' and en_word != which_word:
        win = True

    if win:
        print("correct.")
    else:
        print("incorrect.")

    input("Press Enter to Continue ")
