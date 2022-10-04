print("Welcome to a new game.")

word = input("Count capital and lower letters. Type your word : ")

cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count_cap_letters = 0

small_letters = "abcdefghijklmnopqrstuvwxyz"
count_small_letters = 0


count_consonants = 0
count_vowels = 0

consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"

consonants_tab = []
vowels_tab = []

for x in cap_letters:
    for y in word:
        if x == y:
            count_cap_letters += 1

for x in small_letters:
    for y in word:
        if x == y:
            count_small_letters += 1

for x in consonants:
    for y in word.lower():
        if x == y:
            count_consonants += 1
            consonants_tab.append(y)


for x in vowels:
    for y in word.lower():
        if x == y:
            count_vowels += 1
            vowels_tab.append(y)

print(f"Cap letters : {count_cap_letters} ")
print(f"Small letters : {count_small_letters}")

print(f"Number of consonants : {count_consonants} ")
print(f"consonants : {consonants_tab}")

print(f"Number of vowels : {count_vowels}")
print(f"vowels : {vowels_tab} ")