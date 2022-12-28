from tkinter import *

root = Tk()
root.config(width=600, height=600, pady=10, padx=10)


def selection():
    sel = f"str({var.get()})"
    label.config(text=sel)


var = StringVar()

r1 = Radiobutton(root, text="Male", variable=var, value="M", command=selection)
r1.pack()

r2 = Radiobutton(root, text="Female", variable=var, value="F", command=selection)
r2.pack()

days = []
for day in range(1, 32):
    days.append(day)

months = []
for month in range(1, 13):
    months.append(month)

years = []

for year in range(1910, 2023):
    years.append(year)

day_var = IntVar()
month_var = IntVar()
year_var = IntVar()

days_list = OptionMenu(root, variable=day_var, value=days)
days_list.pack()

label = Label()
label.pack()

root.mainloop()
