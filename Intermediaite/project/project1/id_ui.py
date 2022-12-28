from tkinter import *
from tkinter import ttk

import countries
import check_leap_year
from datetime import date

from model.person import Person

window = Tk()
window.geometry('700x250')
window.resizable(False, False)
window.title("ID")

today = date.today()


# -------------------------- Save a Person -------------------------------- #

def save_person():
    code = 0
    print(e_firstname.get())
    # lastname = e_lastname.get()
    # firstname = e_firstname.get()
    # gender = gender_var.get()
    # day = day_selected.get()
    # month = month_selected.get()
    # year = year_selected.get()
    # dob = f"{year}-{month}-{day}"
    # country = country_selected.get()
    # person_to_save = Person(lastname, e_firstname.get(), gender, dob, country)
    #
    # print(person_to_save.firstname)
    # print(person_to_save.lastname)
    #
    # print(person_to_save.__str__())


# -------------------------- CheckDate ----------------------------------- #
def check_valid_date(event):
    day = day_selected.get()
    month = month_selected.get()
    year = year_selected.get()
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day_selected.set(30)
        days_cb['values'] = [dd for dd in range(1, 31)]
    elif month == 2 and check_leap_year.check_leap(year):
        if day > 29:
            day_selected.set(29)
        days_cb['values'] = [dd for dd in range(1, 30)]
    elif month == 2 and not check_leap_year.check_leap(year):
        if day > 28:
            day_selected.set(28)
        days_cb['values'] = [dd for dd in range(1, 29)]
    else:
        days_cb['values'] = [dd for dd in range(1, 32)]


# -------------------------- CheckKey ------------------------------------- #

def check_key(event):
    value = event.widget.get()
    print(value)


# -------------------------- Label --------------------------------------- #
# Lastname
l_lastname = Label(text="Lastname : ")
l_lastname.grid(column=0, row=1, padx=5, pady=5)

# Firstname
l_firstname = Label(text="Firstname : ")
l_firstname.grid(column=0, row=2, padx=5, pady=5)

# Gender
l_gender = Label(text="Gender : ")
l_gender.grid(column=0, row=3, padx=5, pady=5)

# Calendar
l_dob = Label(text="Birth Date : ")
l_dob.grid(column=0, row=4, padx=5, pady=5)

l_days = Label(text="Day: ")
l_days.grid(column=1, row=4, pady=1, padx=1)
l_months = Label(text="Month : ")
l_months.grid(column=3, row=4, pady=1, padx=1)
l_years = Label(text="Year :")
l_years.grid(column=5, row=4, pady=1, padx=1)

# Nationalities
l_nationality = Label(text="Country : ")
l_nationality.grid(row=2, column=3, padx=1, pady=1)

# Code
l_code = Label(text="ID : ")
l_code.grid(row=1, column=3, padx=1, pady=1)
# ------------------------- Entry ---------------------------------------- #
# Lastname
e_lastname = Entry(width=30)
e_lastname.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

# Firstname
e_firstname = Entry(width=30)
e_firstname.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

# Code
e_code = Entry(width=15)
e_code.grid(row=1, column=5, columnspan=1)
# ------------------------ Button ---------------------------------------- #
search_code = Button(text="Search")
search_code.grid(row=1, column=3)

save = Button(text="Save", command=save_person)
save.grid(row=10, column=2)

# ------------------------ CheckBox ------------------------------------- #

gender_var = StringVar()
gender_var.set("M")
gender_m_radiobutton = Radiobutton(text="M", variable=gender_var, value="M")
gender_m_radiobutton.grid(column=1, row=3, padx=5, pady=5)
gender_f_radiobutton = Radiobutton(text="F", variable=gender_var, value="F")
gender_f_radiobutton.grid(column=2, row=3, padx=5, pady=5)

# ----------------------- Combobox -------------------------------------- #

# Day
day_selected = IntVar()
day_selected.set(today.day)
days_cb = ttk.Combobox(window, textvariable=day_selected, width=5)
days_cb['values'] = [dd for dd in range(1, 32)]
days_cb['state'] = 'readonly'
days_cb.grid(column=2, row=4, padx=1, pady=1)

# Month
month_selected = IntVar()
month_selected.set(today.month)
months_cb = ttk.Combobox(window, textvariable=month_selected, width=5)
months_cb['values'] = [mm for mm in range(1, 13)]
months_cb['state'] = 'readonly'
months_cb.grid(column=4, row=4, padx=1, pady=1)

# Year
year_selected = IntVar()
year_selected.set(today.year)
years_cb = ttk.Combobox(window, textvariable=year_selected, width=5)
years_cb['values'] = [yyyy for yyyy in range(1900, 2023)]
years_cb['state'] = 'readonly'
years_cb.grid(column=6, row=4, padx=1, pady=1)

days_cb.bind('<<ComboboxSelected>>', check_valid_date)
months_cb.bind('<<ComboboxSelected>>', check_valid_date)
years_cb.bind('<<ComboboxSelected>>', check_valid_date)

# Country
country_selected = StringVar()
countries_cb = ttk.Combobox(window, textvariable=country_selected, width=20)
countries_cb['values'] = [values for (key, values) in countries.countries.items()]
countries_cb.grid(row=2, column=5, pady=5, padx=5, columnspan=2)
window.mainloop()
