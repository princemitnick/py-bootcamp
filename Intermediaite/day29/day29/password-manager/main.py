# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.config(pady=20, padx=20, width=200, height=200)
window.title("Password Manager")

canvas = Canvas()

canvas.config(width=200, height=200)
key_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_gen_button = Button(text="Generate Password", highlightthickness=0)
password_gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35)
add_button.grid(columnspan=2, column=1, row=4)



window.mainloop()
