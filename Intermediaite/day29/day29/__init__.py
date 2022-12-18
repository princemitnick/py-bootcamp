import random

min_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
maj_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['#', '%', '@', '!', '&', '(', ')']

min_alphabets_choices = random.randint(1, 3)
maj_alphabets_choices = random.randint(1, 3)
numbers_choices = random.randint(1, 4)
special_characters_choices = random.randint(1, 4)

password_list = []
for _ in range(min_alphabets_choices):
    password_list .append(random.choice(min_alphabets))

for _ in range(maj_alphabets_choices):
    password_list.append(random.choice(maj_alphabets))

for _ in range(numbers_choices):
    password_list.append(random.choice(numbers))

for _ in range(special_characters_choices):
    password_list.append(random.choice(special_characters))

#password_tuple = tuple(password)

print(password_list)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)

# password = ""
# for char in range(0, len(password_tuple)):
#     password += random.choice(password_tuple)
#
# print(password)
