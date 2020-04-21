#OurPyPaint 4/20/2020

import tkinter
from tkinter import *
window = tkinter.Tk()

# -=Window=-

window.geometry('250x250')

window.title("OurPyPaint")

# -=Canvas=-

c = Canvas(window, height=100, width=100, bg="white")

c.pack()

window.mainloop()