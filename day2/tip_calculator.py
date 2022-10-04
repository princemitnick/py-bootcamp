#!/usr/bin/python3

print("Welcome to the tip calculator")

bill_amount = float(input("What was the total bill? : $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? : "))
how_many_people = int(input("How many people to split the bill? : "))

calc_tip = (bill_amount * tip_percentage) / 100
calc_tip += bill_amount

should_pay = calc_tip / how_many_people
print(should_pay)
final_amount = "{:.2f}".format(round(should_pay, 2))
print(f"Each person should pay : ${final_amount}")
