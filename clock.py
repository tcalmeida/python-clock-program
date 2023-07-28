import time
from tkinter import *





window = Tk()
window.title('Clock')

time_label = Label(window, font=('Arial', 50), fg='red', bg='black')
time_label.pack()

day_label = Label(window, font=('Ubuntu', 25))
day_label.pack()

date_label = Label(window, font=('Ubuntu', 25))
date_label.pack()



window.mainloop()
