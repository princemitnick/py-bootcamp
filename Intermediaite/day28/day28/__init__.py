import time
from tkinter import *

def go(count):
    window.after(1000, go, count)
    go_button.config(text="STOP")
    minutes = 24
    seconds = 60
    #count = True

    while count:

        time.sleep(1)
        seconds -= 1
        if seconds == -1:
            minutes -= 1
            seconds = 59

        if len(str(seconds)) == 1:
            seconds_str = f"0{seconds}"
        else:
            seconds_str = seconds

        if len(str(minutes)) == 1:
            minutes_str = f"0{minutes}"
        else:
            minutes_str = minutes

        print(f"{minutes_str}:{seconds_str}")
        label_text = label.config(text=f"{minutes_str}:{seconds_str}")

window = Tk()
window.config(padx=100, pady=100)

label = Label(text=f"00:00")
label.pack()

go_button = Button(text="GO", command=go)
go_button.pack()
window.mainloop()

go(True)


