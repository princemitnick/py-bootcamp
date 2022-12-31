import json
from tkinter import *
from tkinter import messagebox

BG = "white"


def add_new_word():

    def save_new_word():
        fr_word = fr_word_entry.get()
        en_word = en_word_entry.get()

        new_entry = {
            "french": fr_word,
            "english": en_word
        }
        with open("data/data.json", "r") as data_file:
            data = json.load(data_file)

            data.append(new_entry)

        with open("data/data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        save_new_word_window.destroy()

    save_new_word_window = Toplevel(window, padx=50, pady=40, bg=BG)

    fr_word_label = Label(save_new_word_window, text="French Word : ", bg=BG)
    fr_word_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")

    fr_word_entry = Entry(save_new_word_window, width=25, bg=BG, highlightthickness=0)
    fr_word_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    en_word_label = Label(save_new_word_window, text="Meaning : ", bg=BG)
    en_word_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

    en_word_entry = Entry(save_new_word_window, width=25, bg=BG, highlightthickness=0)
    en_word_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    save_word = Button(save_new_word_window, text="Save", command=save_new_word, bg=BG)
    save_word.grid(row=2, column=0, pady=5, padx=5)

    save_new_word_window.mainloop()


window = Tk()
window.title("Flashcard")
window.config(pady=50, padx=50, bg=BG)

add_img = PhotoImage(file="images/add.png")
add_button = Button(image=add_img, highlightthickness=0, bg=BG, command=add_new_word)
add_button.grid(row=0, column=1)

canvas = Canvas(width=612, height=454, highlightthickness=0)
flashcard_img = PhotoImage(file="images/flashcard.png")
canvas.create_image(306, 227, image=flashcard_img)

canvas.create_text(306, 110, text="Hello", font=("Times New Roman", 30, "italic"))

canvas.create_text(306, 180, text="Definition", font=("Times New Roman", 50, "bold"))
canvas.grid(row=1, column=1)

previous_img = PhotoImage(file="images/previous.png")
previous_button = Button(image=previous_img, highlightthickness=0, bg=BG)
previous_button.grid(row=1, column=0)

next_img = PhotoImage(file="images/next.png")
next_button = Button(image=next_img, highlightthickness=0, bg=BG)
next_button.grid(row=1, column=2)

window.mainloop()
