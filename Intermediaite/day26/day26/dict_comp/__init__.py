import pandas

student_dict = {
    "student": ["Prince", "Stanley", "Lovensky"],
    "score": [56, 76, 98]
}

print(student_dict)

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)
for (key, value) in student_data_frame.items():
    print(value)


for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
