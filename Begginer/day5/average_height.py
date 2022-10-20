print("Calculate Average Height")

students_heights = input("Input a list of students heights : ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

total_heights = 0

for x in students_heights:
    total_heights += x

print(f"Total heights : {total_heights}")
print(f"Average : {total_heights / len(students_heights)} ")
