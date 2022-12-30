import json
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import data
import check_leap_year
from datetime import date

from model.person import Person

window = Tk()
window.geometry('700x450')
window.config(bg="white")
window.resizable(False, False)
window.title("ID")

today = date.today()


# -------------------------- Save a Person -------------------------------- #

def save_person():
    code = "A" + str(random.randint(10000, 90000))
    lastname = e_lastname.get()
    firstname = e_firstname.get()
    gender = gender_var.get()
    day = day_selected.get()
    month = month_selected.get()
    year = year_selected.get()
    dob = f"{year}-{month}-{day}"
    country = country_selected.get()

    person = data.get_person(code, lastname, firstname, gender, dob, country)

    try:
        with open("persons.json") as data_file:
            persons = json.load(data_file)
    except FileNotFoundError:
        with open("persons.json", "w") as data_file:
            json.dump(person, data_file, indent=4)
    else:
        persons.update(person)
        with open("persons.json", "w") as data_file:
            json.dump(persons, data_file, indent=4)
    finally:
        data.reset_entry(e_lastname, 0, END)
        data.reset_entry(e_firstname, 0, END)
        gender_var.set("M")
        day_selected.set(today.day)
        month_selected.set(1)
        year_selected.set(today.year)


# --------------------------- Search a Person ----------------------------- #

def search_person():
    try:
        with open("persons.json") as data_file:
            persons = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    else:

        all_codes = data.get_all_codes(persons)
        code = e_code.get()
        if code.strip() == "":
            pass
        elif code not in all_codes:
            messagebox.showinfo(title="Info", message="Person not found")
        else:
            data.reset_entry(search_response, 0, END)
            info = data.showinfo(persons, code)
            print(info)
            search_response.config(state=NORMAL)
            search_response.insert(END, info)
            search_response.config(state=DISABLED)


# -------------------------- CheckDate ----------------------------------- #
def check_valid_date(event):
    day = day_selected.get()
    month = month_selected.get()
    year = year_selected.get()
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day_selected.set(30)
        data.initialize_calendar(days_cb, 1, 31)
    elif month == 2 and check_leap_year.check_leap(year):
        if day > 29:
            day_selected.set(29)
        data.initialize_calendar(days_cb, 1, 30)
    elif month == 2 and not check_leap_year.check_leap(year):
        if day > 28:
            day_selected.set(28)
        data.initialize_calendar(days_cb, 1, 29)
    else:
        data.initialize_calendar(days_cb, 1, 32)


# -------------------------- CheckKey ------------------------------------- #


# -------------------------- Label --------------------------------------- #
# Lastname
l_lastname = Label(text="Lastname : ", bg="white")
l_lastname.grid(column=0, row=1, padx=5, pady=5, sticky='w')

# Firstname
l_firstname = Label(text="Firstname : ", bg="white")
l_firstname.grid(column=0, row=2, padx=5, pady=5, sticky='w')

# Gender
l_gender = Label(text="Gender : ", bg="white")
l_gender.grid(column=0, row=3, padx=5, pady=5, sticky='w')

# Calendar
l_dob = Label(text="Birth Date : ", bg="white")
l_dob.grid(column=0, row=4, padx=5, pady=5, sticky='w')

l_days = Label(text="Day: ", bg="white")
l_days.grid(column=1, row=4, pady=1, padx=1, sticky='w')
l_months = Label(text="Month : ", bg="white")
l_months.grid(column=3, row=4, pady=1, padx=1, sticky='w')
l_years = Label(text="Year :", bg="white")
l_years.grid(column=5, row=4, pady=1, padx=1, sticky='w')

# Nationalities
l_nationality = Label(text="Country : ")
l_nationality.grid(row=2, column=3, padx=1, pady=1, sticky='w')

# Code
l_code = Label(text="ID : ")
l_code.grid(row=1, column=3, padx=1, pady=1, sticky='w')
# ------------------------- Entry ---------------------------------------- #
# Lastname
e_lastname = Entry(width=30)
e_lastname.grid(column=1, row=1, columnspan=2, padx=5, pady=5, sticky='w')

# Firstname
e_firstname = Entry(width=30)
e_firstname.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky='w')

# Code
e_code = Entry(width=15)
e_code.grid(row=1, column=4, columnspan=1, sticky='w')
# ------------------------ Button ---------------------------------------- #
search_code = Button(text="Search", bg="white", command=search_person)
search_code.grid(row=1, column=5, sticky='w')

save = Button(text="Save", command=save_person)
save.grid(row=10, column=3, sticky='w')

# ------------------------ CheckBox ------------------------------------- #

gender_var = StringVar()
gender_var.set("M")
gender_m_radiobutton = Radiobutton(text="M", variable=gender_var, value="M", bg="white")
gender_m_radiobutton.grid(column=1, row=3, padx=5, pady=5, sticky='w')
gender_f_radiobutton = Radiobutton(text="F", variable=gender_var, value="F", bg="white")
gender_f_radiobutton.grid(column=2, row=3, padx=5, pady=5, sticky='w')

# ----------------------- Combobox -------------------------------------- #

# Day
day_selected = IntVar()
day_selected.set(today.day)
days_cb = ttk.Combobox(window, textvariable=day_selected, width=5, background="white")
days_cb['values'] = [dd for dd in range(1, 32)]
data.initialize_calendar(days_cb, 1, 32)
days_cb['state'] = 'readonly'
days_cb.grid(column=2, row=4, padx=1, pady=1, sticky='w')

# Month
month_selected = IntVar()
month_selected.set(today.month)
months_cb = ttk.Combobox(window, textvariable=month_selected, width=5, background="white")
data.initialize_calendar(months_cb, 1, 13)
months_cb['state'] = 'readonly'
months_cb.grid(column=4, row=4, padx=1, pady=1, sticky='w')

# Year
year_selected = IntVar()
year_selected.set(today.year)
years_cb = ttk.Combobox(window, textvariable=year_selected, width=5, background="white")
data.initialize_calendar(years_cb, 1900, today.year)
years_cb['state'] = 'readonly'
years_cb.grid(column=6, row=4, padx=1, pady=1, sticky='w')
days_cb.bind('<<ComboboxSelected>>', check_valid_date)
months_cb.bind('<<ComboboxSelected>>', check_valid_date)
years_cb.bind('<<ComboboxSelected>>', check_valid_date)

# Country
country_selected = StringVar()
countries_cb = ttk.Combobox(window, textvariable=country_selected, width=20, background="white")
countries_cb['values'] = [values for (key, values) in data.countries.items()]
countries_cb.grid(row=2, column=4, pady=5, padx=5, columnspan=3, sticky='w')

# ------------------------------------ Text -------------------------------------------------- #
search_response = Text(state=DISABLED, bg="white", width=55, height=15)
search_response.grid(pady=5, padx=5, row=12, column=1, columnspan=4, sticky='w')

window.mainloop()
