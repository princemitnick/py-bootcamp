list_1 = []
list_2 = []

with open("file1.txt") as file1:
    for line in file1:
        list_1.append(int(line))

with open("file2.txt") as file2:
    for line in file2:
        list_2.append(int(line))

with open("file1.txt") as file1:
    list_n_1 = [int(line) for line in file1]

with open("file2.txt") as file2:
    list_n_2 = [int(line) for line in file2]

print(list_1)
print(list_2)

print(list_n_1)
print(list_n_2)

common_number = [
    n for n in list_n_1 if n in list_n_2
]

print(common_number)