#!/usr/bin/python3

height = int(input("Height : "))

if height > 120:
    print("run")
    age = int(input("Age : "))
    if age < 12:
        print("Pay $5.")
    elif age <= 18:
        print("Pay $7.")
    else:
        print("Pay $12.")
else:
    print("Cannot run")