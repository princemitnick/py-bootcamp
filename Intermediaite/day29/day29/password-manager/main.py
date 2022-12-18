import random
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    min_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    maj_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['#', '%', '@', '!', '&', '(', ')']

    nr_min_alphabets = random.randint(2, 3)
    nr_maj_alphabets = random.randint(2, 3)
    nr_numbers = random.randint(1, 4)
    nr_special_characters = random.randint(1, 4)

    password_min_alphabets = [random.choice(min_alphabets) for _ in range(nr_min_alphabets)]
    password_maj_alphabets = [random.choice(maj_alphabets) for _ in range(nr_maj_alphabets)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_special_characters = [random.choice(special_characters) for _ in range(nr_special_characters)]

    password_list = password_min_alphabets + password_maj_alphabets + password_numbers + password_special_characters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_site = website_entry.get()
    email_input = email_username_entry.get()
    password_input = password_entry.get()
    if len(web_site) == 0 or len(password_input) == 0 or len(email_input) == 0:
        messagebox.showinfo(title="Error", message="email, password or email field cannot be empty")
    elif messagebox.askokcancel(title=web_site,
                                message=f"These are details entered: \nEmail : {email_input} \nPassword: {password_input}"
                                        f"\nIs it ok to save?"):
        with open("data.txt", "a") as file:
            file.write(f"{web_site} | {email_input} | {password_input}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        pass


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.config(pady=50, padx=50, width=200, height=200, bg="white")
window.title("Password Manager")

canvas = Canvas()

canvas.config(width=200, height=200, bg="white")
key_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg="white")
label_website.grid(column=0, row=1)
email_username_label = Label(text="Email/Username: ", bg="white")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, "ingjeanbaptiste@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_gen_button = Button(text="Generate Password", highlightthickness=0, bg="white", command=password_generator)
password_gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, bg="white", command=save_password)
add_button.grid(columnspan=2, column=1, row=4)

window.mainloop()
