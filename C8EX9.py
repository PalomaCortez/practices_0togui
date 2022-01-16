## Cap 8 - GUI
# EX10 - Menu Demo
# OBS .png files are not being read

from tkinter import *


class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        # create a new menu bar
        menu_bar = Menu(window)
        window.config(menu=menu_bar)  # display the menu bar

        # Create a pull-down menu, and add it to the menu bar
        operation_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Operation", menu=operation_menu)
        operation_menu.add_command(label="Add", command=self.add)
        operation_menu.add_command(label="Subtract", command=self.subtract)
        operation_menu.add_separator()
        operation_menu.add_command(label="Multiply", command=self.multiply)
        operation_menu.add_command(label="Divide", command=self.divide)

        # Create more pull-down menus
        exit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Exit", menu=exit_menu)
        exit_menu.add_command(label="Quit", command=window.quit)

        # add a tool bar frame
        frame0 = Frame(window)
        frame0.grid(row=1, column=1, sticky=W)

        # create images
        plus_image = PhotoImage(file="image/plus.png")
        minus_image = PhotoImage(file="image/minus.png")
        times_image = PhotoImage(file="image/times.png")
        divide_image = PhotoImage(file="image/divide.png")

        Button(frame0, image=plus_image,
               command=self.add).grid(row=1, column=1, sticky=W)
        Button(frame0, image=minus_image,
               command=self.subtract).grid(row=1, column=2)
        Button(frame0, image=times_image,
               command=self.multiply).grid(row=1, column=3)
        Button(frame0, image=divide_image,
               command=self.divide).grid(row=1, column=4)

        frame1 = Frame(window)
        frame1.grid(row=2, column=1, pady=10)
        Label(frame1, text="Number 1:").pack(side=LEFT)
        self.v1 = StringVar()
        Entry(frame1, width=5, textvariable=self.v1,
              justify=RIGHT).pack(side=LEFT)
        Label(frame1, text="Number 2:").pack(side=LEFT)
        self.v2 = StringVar()
        Entry(frame1, width=5, textvariable=self.v2,
              justify=RIGHT).pack(side=LEFT)
        Label(frame1, text="Result:").pack(side=LEFT)
        self.v3 = StringVar()
        Entry(frame1, width=5, textvariable=self.v3,
              justify=RIGHT).pack(side=LEFT)

        # add buttons to frame2
        frame2 = Frame(window)
        Button(frame2, text="Add", command=self.add).pack(
            side=LEFT)
        Button(frame2, text="Subtract", command=self.subtract
               ).pack(side=LEFT)
        Button(frame0, text="Multiply", command=self.multiply
               ).pack(side=LEFT)
        Button(frame0, text="Divide", command=self.divide
               ).pack(side=LEFT)

        mainloop()

    def add(self):
        self.v3.set(eval(self.v1.get()) + (eval(self.v2.get())))

    def subtract(self):
        self.v3.set(eval(self.v1.get()) - (eval(self.v2.get())))

    def multiply(self):
        self.v3.set(eval(self.v1.get()) * (eval(self.v2.get())))

    def divide(self):
        self.v3.set(eval(self.v1.get()) / (eval(self.v2.get())))


MenuDemo()
