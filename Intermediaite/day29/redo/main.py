import random

min_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
maj_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['#', '%', '@', '!', '&', '(', ')']

nr_min_alphabets = random.randint(2, 3)
nr_maj_alphabets = random.randint(2, 3)

nr_numbers = random.randint(1, 4)
nr_special_characters = random.randint(1, 4)


password_min_alphabets = [random.choice(min_alphabets) for _ in range(nr_min_alphabets)]
password_maj_alphabets = [random.choice(maj_alphabets) for _ in range(nr_maj_alphabets)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
password_special_characters = [random.choice(special_characters) for _ in range(nr_special_characters)]

password_list = password_min_alphabets + password_maj_alphabets + password_numbers + password_special_characters

random.shuffle(password_list)
print("".join(password_list))