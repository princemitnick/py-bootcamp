# from tkinter import *
# from tkinter.tix import ComboBox
#
# window = Tk()
# window.geometry('300x300')
#
# label = Label(text="Select the Month :")
# label.grid(column=0, row=15, padx=10, pady=25)
#
# var = StringVar()
#
# monthchoosen = ComboBox()
#
# window.mainloop()


import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
# Label
ttk.Label(window, text="Select the Month :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=15, padx=10, pady=25)

n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width=27,
                            textvariable=n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column=1, row=15)

# Shows february as a default value
monthchoosen.current(1)
window.mainloop()
