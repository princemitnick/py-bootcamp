import turtle
import pandas
from dept_obj import HaitiDepartment
screen = turtle.Screen()
screen.setup(width=900, height=800)
image = "./haiti-blank-map.gif"
screen.addshape(image)
tim = turtle.Turtle()
tim.shape(image)

haiti_departments = pandas.read_csv("haiti-department.csv")
haiti_departments_name = haiti_departments['department'].to_list()

print(haiti_departments_name)

guess_department = []
dept_count = 0

while dept_count != 10:
    dept_answer = screen.textinput(title=f"{dept_count}/10", prompt="Department : ").title()
    if dept_answer not in haiti_departments_name or dept_answer in guess_department:
        print(dept_answer)
        pass
    else:
        department_data = haiti_departments[haiti_departments['department'] == dept_answer]
        department_xcor = int(department_data.x)
        department_ycor = int(department_data.y)
        print(dept_answer)
        guess_department.append(dept_answer)
        HaitiDepartment(dept_answer, department_xcor, department_ycor)
        dept_count += 1

turtle.mainloop()