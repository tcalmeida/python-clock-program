import time
from tkinter import *

def update_clock():
    display_time = time.strftime('%H:%M:%S')
    time_label.config(text=display_time)

    display_day = time.strftime('%A')
    day_label.config(text=display_day)

    display_date = time.strftime('%B %d, %Y')
    date_label.config(text=display_date)

    window.after(1000, update_clock)



window = Tk()
window.title('Clock')

time_label = Label(window, font=('Arial', 50), fg='red', bg='black')
time_label.pack()

day_label = Label(window, font=('Ubuntu', 25))
day_label.pack()

date_label = Label(window, font=('Ubuntu', 25))
date_label.pack()

update_clock()

window.mainloop()
