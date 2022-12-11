import time
from tkinter import *


def go(minutes, seconds):
    # count = True
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
    n_text = f"{minutes_str}:{seconds_str}"
    canvas.itemconfig(timer_text, text=n_text)
    window.after(1000, go, minutes, seconds)

def start():
    go(24, 60)

window = Tk()
window.config(padx=100, pady=100)

canvas = Canvas(width=50, height=50)
timer_text = canvas.create_text(20, 20, text="00:00")
canvas.pack()

go_button = Button(text="Go", command=start)
go_button.pack()


window.mainloop()
