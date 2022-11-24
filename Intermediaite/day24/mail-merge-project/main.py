STARTING_LETTER = "./Input/Letters/starting_letter.txt"
INVITED_NAMES = "./Input/Names/invited_names.txt"
TO_SEND = "./Output/ReadyToSend"

names = []


with open(STARTING_LETTER, "r") as letter:
    letter_for_invited = letter.read()
with open(INVITED_NAMES, "r") as invited_names:
    for name in invited_names:
        names.append(name.rstrip())


for name in names:
    with open(f"{TO_SEND}/letter_for_{name}.txt", "w") as new_letter:
        print(name)
        new_letter_for_invited = letter_for_invited.replace("[Name]", name)
        new_letter.write(new_letter_for_invited)

