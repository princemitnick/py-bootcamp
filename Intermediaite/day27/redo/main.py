from tkinter import *

window = Tk()
window.geometry("300x200")
window.config(padx=10, pady=10)


def calculate():
    try:
        get_value = int(entry.get())
    except ValueError:
        print("number only")
    else:
        miles = get_value * round(1.600934, 2)
        label2.config(text=f"is equal to {miles} Km")


entry = Entry()
entry.grid(row=1, column=1)

label1 = Label(window, text="Miles")
label1.grid(column=2, row=1)

value = 0
label2 = Label(text=f"is equal to {value} Km")
label2.grid(row=2, column=1)

calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1)

window.mainloop()
