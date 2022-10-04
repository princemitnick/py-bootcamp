print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? : "))
bill = 0
if height > 120:
    print("You can ride a rollercoaster.")
    age = int(input("What is your age? : "))
    if age < 12:
        print("You have to pay $5.")
        bill = 5
    elif age < 18:
        print("You have to pay $7.")
        bill = 7
    else:
        print("You have to pay $12.")
        bill = 12

    wants_photo = str(input("Do you want to take a photo? (Y/N)"))
    if wants_photo.__eq__("Y") | wants_photo.__eq__("y"):
        bill += 3
        print(f"Your bill is {bill}")
    else:
        print(f"Your bill is {bill}")

else:
    print("You have to grow taller before you can ride")