#!/usr/bin/python3

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = round(weight / (height**2))
print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")

