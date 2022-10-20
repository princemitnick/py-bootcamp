#!/usr/bin/python3
# Data Types

# String

name = input("Enter your whole name : ")
strip_name = name.replace(" ","")
print("Your name contains ", len(strip_name), "characters without space.")
print("your name contains ", len(name), "characters with space.")

# Int
print(type(123_456_789))

# Boolean

# Float

print(70 + float("100.5"))

print(3 * (3 + 3) / 3 - 3)
