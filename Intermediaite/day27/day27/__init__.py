import random
import time
import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width=500, height=300)

# Label

label = Label(text="Label 1", font=("Times New Roman", 14, "italic"))
label.pack(side="left")

label["text"] = "New Text"
label.config(text="New texto")

a = Label(text="a")
a.pack()
text_input_1 = Entry()
text_input_1.pack()
b = Label(text="b")
b.pack()
text_input_2 = Entry()
text_input_2.pack()
def new_label():
    a = int(text_input_1.get())
    b = int(text_input_2.get())
    label["text"] = f"{a + b}"



def button_clicked():
    new_label()
    print("I got clicked")


like = Button(fg="red", bg="blue", text="Click on Me", command=button_clicked)
like.pack(side="left")

window.mainloop()
