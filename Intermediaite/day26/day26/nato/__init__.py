import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

print(nato_phonetic_alphabet)

name = "Prince"

name_to_list = [letter.upper() for letter in name]
print(name_to_list)

#for letter in name_to_list:
#    for (index, row) in nato_phonetic_alphabet.iterrows():
#        if letter == row.letter:
#           print(row.letter, row.code)

nato_to_dict = {
    row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()
}

print(nato_to_dict)

extract = [nato_to_dict[letter] for letter in name_to_list]

# extract_2 = [
#     code for (letter, code) in nato_to_dict.items() if letter in name_to_list
# ]
#
# print(extract_2)
#
# extract = []
#
# for letter in name_to_list:
#     for (key, value) in nato_to_dict.items():
#         if letter == key:
#             extract.append(value)

print(extract)