import json
import random
from json import JSONDecodeError
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
    pyperclip.paste()


# --------------------------------SEARCH WEBSITE----------------------------- #

def search_website():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="Data not found", title="Error")
    else:
        website_list = []
        website_to_search = website_entry.get()
        print(website_to_search)
        for (key, values) in data.items():
            print(key)
            website_list.append(key)
        print(website_list)
        if website_to_search not in website_list:
            print(type(website_to_search))
            messagebox.showinfo(title="Info", message=f"{website_to_search} not found")
        else:
            email = data[website_to_search]["email"]
            password = data[website_to_search]["password"]
            messagebox.showinfo(title=f"{website_to_search} found.", message=f"Email : {email} \nPassword : {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web_site = website_entry.get()
    email_input = email_username_entry.get()
    password_input = password_entry.get()

    new_data = {
        web_site: {
            "email": email_input,
            "password": password_input
        }
    }

    if len(web_site) == 0 or len(password_input) == 0 or len(email_input) == 0:
        messagebox.showinfo(title="Error", message="email, password or email field cannot be empty")
    elif messagebox.askokcancel(title=web_site,
                                message=f"These are details entered: \nEmail : {email_input} \nPassword: {password_input}"
                                        f"\nIs it ok to save?"):
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
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

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
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

search_button = Button(text="Search", width=8, highlightthickness=0, bg="white", command=search_website)
search_button.grid(column=3, row=1)

window.mainloop()
