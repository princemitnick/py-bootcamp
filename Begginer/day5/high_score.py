print("High score")

students_score = input("Enter the students score : ").split()

for x in range(0, len(students_score)-1):
    students_score[x] = int(students_score[x])

max_score = 0
for x in students_score:
    if int(x) >= max_score:
        max_score = int(x)


print(f"max : {max_score}")