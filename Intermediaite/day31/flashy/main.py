from tkinter import *
import pandas

BACKGROUND = "#B1DDC6"


def next_card():
    to_learn = pandas.read_csv("./data/french_words.csv")
    print(to_learn.to_dict(orient="records"))


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=1)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=2, column=0)

check_image = PhotoImage(file="./images/right.png")
know_button = Button(image=check_image, highlightthickness=0, command=next_card)
know_button.grid(row=2, column=2)

window.mainloop()
