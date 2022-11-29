numbers = [1, 2, 3]

# new_list  = numbers
# for n in new_list:
#     print(n)

new_list = [
    n
    for n in numbers
]
print(new_list)

name = "Prince"
name_to_list_of_letters = [letter.upper() for letter in name]

#print(name_to_list_of_letters)

double_list = [ n * 2 for n in range(1, 5)]

print(double_list)

cond_list = [n for n in double_list if n < 6]

print(cond_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) == 4]

print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)


n_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n ** 2 for n in n_numbers]

print(squared_numbers)

f_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [n for n in f_numbers if n % 2 == 0]

print(result)