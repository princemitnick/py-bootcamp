from tkinter import *


window = Tk()
window.minsize(width=400, height=100)
window.config(padx=100, pady=100)

input = Entry(width=10)
input.grid(column=2, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=3, row=1)


label_miles = Label(text=f"is equal to {0} KM")
label_miles.grid(column=2, row=2)
label_miles.config(padx=10, pady=10)


def calculate_km():
    km = round(int(input.get()) * 1.609)
    label_miles.config(text=f"is equal to {km} KM")


button = Button(text="Calculate", command=calculate_km)
button.grid(column=3, row=3)

window.mainloop()