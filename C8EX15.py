## Cap 8 - GUI
# Ex15 - Scroll Text demo

from tkinter import *


class ScrollText:
    def __init__(self):
        window = Tk()
        window.title("Scroll Text Demo")

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)  # the scrollbar is contained on th frame not on the full window
        scrollbar.pack(side=RIGHT, fill=Y)
        text = Text(frame1, width=40, height=10, wrap=WORD,
                    yscrollcommand=scrollbar.set)
        text.pack()
        scrollbar.config(command=text.yview)

        window.mainloop()


ScrollText()
