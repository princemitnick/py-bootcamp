print("Day 9")

notes = {
    "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ],
    "months":[
        "January",
        "February",
        "March",
        "May",
        "April",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
}
print("Days : ")
for x in notes["days"]:
    print(x, end=",")
print("\n")
print("Months : ")
for y in notes["months"]:
    print(y, end=",")

#notes["programming"] = {
#    "loop": "The action of doing something over and over again",
#    "bug": "An error in a program that prevents the program from running as expected",
#}

print("\n")
for x in notes:
    print(f"{x} : {notes[x][0]}")
