#!/usr/bin/python3
# var1 = int(input("Enter two digits : "))
# var2 = int(input())

# print("Sum of ", var1, " + ", var2, " is : ", var1+var2)

two_digit_number = input("Type two digit number")
try:
    var1 = int(two_digit_number[0])
    var2 = int(two_digit_number[1])
    print("Sum of ", var1, " + ", var2, " is : ", var1 + var2)
except:
    print("problem")

