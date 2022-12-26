import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(nato_phonetic_alphabet)


def generate_phonetic():
    name = input("Enter a word : ").upper()
    name_to_list = [letter for letter in name]
    nato_to_dict = {
        row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()
    }
    try:
        extracted_words = [nato_to_dict[letter] for letter in name_to_list]
    except KeyError as key_err_msg:
        print(f"Sorry, only letters in the alphabet please. {key_err_msg}")
        generate_phonetic()
    else:
        print(extracted_words)

generate_phonetic()