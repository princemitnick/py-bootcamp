#!/usr/bin/python3

age = int(input("What is your current age : "))

years_left = 90 - age

weeks_left = years_left * 52

days_left = years_left * 365

months_left = years_left * 12

print(f"You {days_left} days, {weeks_left} weeks and {months_left} months left.")