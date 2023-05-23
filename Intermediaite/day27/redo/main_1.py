from tkinter import *

window = Tk()
window.config(padx=10, pady=10)
window.geometry("500x300")
window.title("Page 1")


def button_clicked():
    lab1.config(text="Button clicked")


def reset_label():
    lab1.config(text="Hello")


lab1 = Label(window, text="Hello")
lab1.grid(row=0, column=0)

but = Button(window, text="Ok", command=button_clicked)
but.grid(row=1, column=0)

reset = Button(window, text="Reset", command=reset_label)
reset.grid(row=1, column=1)

window.mainloop()
