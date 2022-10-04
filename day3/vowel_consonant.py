print("Welcome to a new game.")

word = input("Count capital and lower letters. Type your word : ")

cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count_cap_letters = 0

small_letters = "abcdefghijklmnopqrstuvwxyz"
count_small_letters = 0


consonants = "bcdefghjklmnpqrstvwxz"
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
            consonants_tab.append(y)

for x in vowels:
    for y in word.lower():
        if x == y:
            vowels_tab.append(y)

print(f"Cap letters : {count_cap_letters} ")
print(f"Small letters : {count_small_letters}")

print(f"consonants : {consonants_tab}")
print(f"vowels : {vowels_tab} ")