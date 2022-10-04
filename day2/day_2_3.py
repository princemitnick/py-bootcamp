#!/usr/bin/python3

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weigh in kg : "))

bmi = int(weight / (height**2))

print("Your BMI is : ", bmi)