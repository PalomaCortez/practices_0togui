## Cap 8 - GUI
# EX1 - tkinter module and simple GUI

from tkinter import *

window = Tk()  # create a window
label = Label(window, text="Welcome to Python")  # create a label
button = Button(window, text="Click Me")  # create a button
label.pack()  # place the label in he window
button.pack()  # place the button in the wondow


window.mainloop()

# every in here would be bloked until the window is closed


