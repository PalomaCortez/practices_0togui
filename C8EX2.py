## Cap 8 - GUI
# EX2 - Process Button Event


from tkinter import *


def process_ok():
    print("The button is clicked")


def process_cancel():
    print("Cancel button is clicked")


window = Tk()  # create a window
bt_ok = Button(window, text="OK", fg='red', command=process_ok)
bt_cancel = Button(window, text="Cancel", bg='yellow', command=process_cancel)
bt_ok.pack()  # place the button in the window
bt_cancel.pack()

window.mainloop()

# every in here would be blocked until the window is closed
