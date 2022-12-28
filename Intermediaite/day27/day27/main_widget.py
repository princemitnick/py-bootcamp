from tkinter import *

# Creating a new Window and configurations

window = Tk()
window.title("Prince Widgets")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
#label.pack()


# Buttons
def action():
    print("Do Something")
    print(entry.get())
    print(spinbox.get())
    print(scale.get())


button = Button(text="Click Me", command=action)
#button.pack()

# Entries
entry = Entry(width=30)

# Add some text to begin with
entry.insert(END, string="Some text to begin with")
print(entry.get())
#entry.pack()

# Text
text = Text(height=5, width=30)

# Puts the cursor in textbox
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 1
print(text.get("1.0", END))
#text.pack()


# Spinbox

def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
#spinbox.pack()


# Scale

def scaled_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scaled_used)
#scale.pack()


# Checkbutton

def checkbutton_used():
    # Print 1 if On button checked, otherwise 0.
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
checkbutton.grid(column=0, row=40)


# Radiobutton

def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
#radiobutton1.pack()
#radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    #print(listbox.get(listbox.curselection()))
    print(listbox2.get(listbox2.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=2, row=40)

listbox2 = Listbox(height=10)
numbers = []
for index in range(0, 10):
    listbox2.insert(index, index)

#listbox2.pack()
listbox2.bind("<<ListboxSelect>>", listbox_used)


options = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

clicked = StringVar()


window.mainloop()
