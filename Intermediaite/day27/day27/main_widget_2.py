from tkinter import *

window = Tk()
window.minsize(width=400, height=300)
window.config(padx=100, pady=200)

fn_label = Label(text="First number")
fn_label.grid(column=0, row=0)
fn_label.config(padx=50, pady=50)

fn_entry = Entry(width=10)
fn_entry.grid(column=1, row=0)


sn_label = Label(text="Second number")
sn_label.grid(column=0, row=1)
sn_label.config(padx=50, pady=50)

sn_entry = Entry(width=10)
sn_entry.grid(column=2, row=1)


my_button = Button(text="Ok")
my_button.grid(column=0, row=2)
my_button.config(padx=50, pady=50)
window.mainloop()