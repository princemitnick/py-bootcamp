from tkinter import *

window = Tk()
window.config(bg="white", padx=5, pady=5)

q_canvas = Canvas(width=612, height=454, bg="white")
q_canvas.grid(row=1, column=1, columnspan=2)

true_im = PhotoImage(file="./data/images/true.png")
true_button = Button(image=true_im, bg="white", highlightthickness=0, highlightcolor="white")
false_im = PhotoImage(file="./data/images/false.png")
false_button = Button(image=false_im, bg="white", highlightthickness=0, highlightcolor="white")
true_button.grid(row=2, column=1)
false_button.grid(row=2, column=2)

window.mainloop()
