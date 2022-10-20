#!/usr/bin/python3

year = int(input("Which year do you want to check? "))

#if (year % 4 == 0 & year % 100 != 0) | year % 400 == 0:
#    print("leap")
#else:
#    print("not leap")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap")
        else:
            print("Not leap")
    else:
        print("Leap")
else:
    print("Not leap year")
