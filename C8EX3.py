## Cap 8 - GUI
# EX3 - Widgets Demo

from tkinter import *


class WidgetsDemo:
    def __init__(self):
        window = Tk()  # create a window
        window.title("Widgets Demo")  # set a title

        # add a check button, and a radio button to frame1
        frame1 = Frame(window)  # create and add a frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbt_bold = Checkbutton(frame1, text="Bold", variable=self.v1,
                                command=self.process_checkbutton)
        self.v2 = IntVar()
        rb_red = Radiobutton(frame1, text="Red", bg="red",
                             variable=self.v2, value=1,
                             command=self.process_radiobutton)
        rb_yellow = Radiobutton(frame1, text="Yellow",
                                bg="yellow", variable=self.v2, value=2,
                                command=self.process_radiobutton)
        cbt_bold.grid(row=1, column=1)
        rb_red.grid(row=1, column=2)
        rb_yellow.grid(row=1, column=3)

        # add a label, an entry, a button and a message to frame1
        frame2 = Frame(window)  # create and add a frame to the window
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        self.name = StringVar()
        entry_name = Entry(frame2, textvariable=self.name)
        bt_get_name = Button(frame2, text="Get Name",
                             command=self.process_button)
        message = Message(frame2, text="This is a Widgets Demo")
        label.grid(row=1, column=1)
        entry_name.grid(row=1, column=2)
        bt_get_name.grid(row=1, column=3)
        message.grid(row=1, column=4)

        # add text
        text = Text(window)
        text.pack()
        text.insert(END,
                    "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END,
                    "these carefully designed examples and use then ")
        text.insert(END, "to create your applications.")

        window.mainloop()

    def process_checkbutton(self):
        print("Check button is "
              + ("checked" if self.v1.get() == 1 else "unchecked"))

    def process_radiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow")
              + " is selected ")

    def process_button(self):
        print("Your name is " + self.name.get())


WidgetsDemo()  #create GUI
