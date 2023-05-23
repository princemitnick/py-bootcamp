from tkinter import *

import requests

window = Tk()
window.geometry("500x300")


def get_quote():
    URL = "https://api.kanye.rest/"
    response = requests.get(URL)
    return response.json()['quote']


def new_quote():
    quote = get_quote()
    lab1.config(text=quote)


lab1 = Label(window, text=get_quote())
lab1.pack()


but1 = Button(window, text="New", command=new_quote)
but1.pack()


window.mainloop()
