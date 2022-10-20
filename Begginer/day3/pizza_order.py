print("Welcome to Python Pizza Devileries!")

size = input("What size pizza do you want>? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra? Y or N : ")
bill = 0

if size == 'S':
    print("Small pizza costs $15.")
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill = 15 + 2
    else:
        bill = 15
elif size == 'M':
    print("Medium pizza costs $20.")
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill = 20 + 3
    else:
        bill = 20
elif size == 'L':
    print("Large pizza costs $25.")
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill = 25 + 3
    else:
        bill = 25

if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 1
    print(f"Your final bill is : {bill}")
else:
    print(f"Your final bill is {bill}")
