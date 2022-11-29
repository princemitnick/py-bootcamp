with open("file1.txt") as file1:
    list_n_1 = [int(line) for line in file1]

with open("file2.txt") as file2:
    list_n_2 = [int(line) for line in file2]


print(f"List from file1.txt : \n{list_n_1}")
print(f"List from file2.txt : \n{list_n_2}")

common_number = [
    n for n in list_n_1 if n in list_n_2
]

print(f"Common line in file1.txt and file2.txt : \n{common_number}")
