import random

print("Banker Roulette!")

list_names = input("Enter the list of names separete by a coma (,) : ")

names = list_names.split(",")
choice = random.randint(0, len(names)-1)
print(f"{names[choice]} is going to pay the bill to day!")

print(random.choice(names))