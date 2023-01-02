import json
import random
from tkinter import *
from tkinter import messagebox

BG = "white"


def fr_dictionary():
    with open("./data/data.json") as dict_file:
        return json.load(dict_file)


def fr_words_list():
    dictionary = fr_dictionary()
    french_words = []
    for index in dictionary:
        french_words.append(index['french'])
    return french_words


def add_new_word():
    def save_new_word():
        fr_word = fr_word_entry.get().lower()
        en_word = en_word_entry.get().lower()

        if fr_word in fr_words_list():
            messagebox.showinfo(title=f"{fr_word}", message=f"{fr_word} already existed")
        elif fr_word.strip() == "" or en_word.strip() == "":
            pass
        else:
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

    # canvas_win2 = Canvas(save_new_word_window, width=64, height=64)
    # notebook_img = PhotoImage(file="images/notebook.png")
    # canvas.create_image(32, 32, image=notebook_img)
    # canvas_win2.grid(row=2, column=0, pady=5, padx=5)

    fr_word_label = Label(save_new_word_window, text="French Word : ", bg=BG, font=("Times New Roman", 12, "bold"))
    fr_word_label.grid(row=1, column=1, pady=3, padx=3, sticky="w")

    fr_word_entry = Entry(save_new_word_window, width=25, bg=BG, highlightthickness=0)
    fr_word_entry.grid(row=1, column=2, padx=3, pady=3, sticky='w')

    en_word_label = Label(save_new_word_window, text="Meaning : ", bg=BG, font=("Times New Roman", 12, "bold"))
    en_word_label.grid(row=2, column=1, pady=3, padx=3, sticky='w')

    en_word_entry = Entry(save_new_word_window, width=25, bg=BG, highlightthickness=0)
    en_word_entry.grid(row=2, column=2, padx=3, pady=3, sticky='w')

    save_word = Button(save_new_word_window, text="Save", font=("Times New Roman", 12, "bold"), command=save_new_word,
                       bg=BG)
    save_word.grid(row=3, column=1, pady=3, padx=3)

    save_new_word_window.mainloop()


def list_words():
    fr_dict = fr_dictionary()
    list_word_window = Toplevel(window, padx=50, pady=40, bg=BG)
    list_word_window.title("Dictionary")
    list_word_window.geometry("700x600")
    scrollbar = Scrollbar(list_word_window, orient='vertical')
    scrollbar.pack(side=LEFT, fill=BOTH)
    # scrollbar.grid(column=0, row=0)
    dico = Listbox(list_word_window, width=30, height=150, font=("Times New Roman", 14, "bold"))
    # dico.grid(column=0, row=0)
    dico.pack(side=LEFT, fill=BOTH)
    dico.config(yscrollcommand=scrollbar.set)
    print(fr_dict)
    for item in fr_dict:
        print(f"{item['french']} - {item['english']}")
        dico.insert(END, f"{item['french'].upper()} : {item['english']}")

    scrollbar.config(command=dico.yview)

def next_word():
    fr_dict = fr_dictionary()
    fr_content = canvas.itemcget(current_fr_word, 'text')
    en_content = canvas.itemcget(current_en_word, 'text')
    index = fr_dict.index({
        "french": fr_content,
        "english": en_content
    })
    if index == len(fr_dict) - 1:
        pass
    else:
        canvas.itemconfig(current_fr_word, text=f"{fr_dict[index + 1]['french']}")
        canvas.itemconfig(current_en_word, text=f"{fr_dict[index + 1]['english']}")


def previous_word():
    fr_dict = fr_dictionary()
    fr_content = canvas.itemcget(current_fr_word, 'text')
    en_content = canvas.itemcget(current_en_word, 'text')
    index = fr_dict.index({
        "french": fr_content,
        "english": en_content
    })
    if index == 0:
        pass
    else:
        canvas.itemconfig(current_fr_word, text=f"{fr_dict[index - 1]['french']}")
        canvas.itemconfig(current_en_word, text=f"{fr_dict[index - 1]['english']}")


window = Tk()
window.title("Flashcard")
window.config(pady=50, padx=50, bg=BG)

add_img = PhotoImage(file="images/add.png")
add_button = Button(image=add_img, highlightthickness=0, bg=BG, command=add_new_word)
add_button.grid(row=0, column=0, columnspan=1)

list_img = PhotoImage(file="images/list.png")
list_button = Button(image=list_img, highlightthickness=0, bg=BG, command=list_words)
list_button.grid(row=0, column=1, columnspan=1)

canvas = Canvas(width=612, height=454, highlightthickness=0)
flashcard_img = PhotoImage(file="images/flashcard.png")
canvas.create_image(306, 227, image=flashcard_img)

fr_dict = fr_dictionary()

random_ind = random.randint(0, len(fr_dict) - 1)
current_fr_word = canvas.create_text(306, 110, text=f"{fr_dict[random_ind]['french']}",
                                     font=("Times New Roman", 30, "italic"), fill="blue")
current_en_word = canvas.create_text(306, 208, text=f"{fr_dict[random_ind]['english']}",
                                     font=("Times New Roman", 50, "bold"))
canvas.grid(row=1, column=1, columnspan=3)

previous_img = PhotoImage(file="images/previous.png")
previous_button = Button(image=previous_img, highlightthickness=0, bg=BG, command=previous_word)
previous_button.grid(row=1, column=0)

next_img = PhotoImage(file="images/next.png")
next_button = Button(image=next_img, highlightthickness=0, bg=BG, command=next_word)
next_button.grid(row=1, column=5)

window.mainloop()
