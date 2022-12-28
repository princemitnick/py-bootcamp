import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

window = tk.Tk()

# Config the root window
window.geometry('300x200')
window.resizable(False, False)
window.title("Combo Testing")

# Label
label = tk.Label(text="Please select a month:")
label.pack(fill=tk.X, pady=5, padx=5)

# Create a Combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(window, textvariable=selected_month)
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

month_cb['state'] = 'readonly'
month_cb.pack(fill=tk.X, padx=5, pady=5)


def month_changed(event):
    showinfo(title='Result', message=f"You selected {selected_month.get()}!")


month_cb.bind('<<ComboboxSelected>>', month_changed)

window.mainloop()