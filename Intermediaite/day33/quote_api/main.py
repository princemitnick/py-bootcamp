from tkinter import *

import requests


def get_quote():
    URL = "https://api.kanye.rest/"
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()["quote"]


def new_quote():
    quote = get_quote()
    canvas.itemconfig(text, text=quote)


tk = Tk()
tk.config(background="white")
tk.geometry("650x500")

canvas = Canvas(width=612, height=454, highlightthickness=0)
background_img = PhotoImage(file="./flashcard.png")
canvas.create_image(306, 227, image=background_img)

text = canvas.create_text(306, 180, text="", fill="red", font=("Consolas", 15, "italic"), width=150)

canvas.grid(column=1, row=1)

button = Button(text="New", background="white", command=new_quote)
button.grid(column=1, row=2)

tk.after(2000, func=new_quote)

tk.mainloop()
