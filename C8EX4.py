## Cap 8 - GUI
# EX4 - Change label demo

from tkinter import *


class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Change Label Demo")

        # add a label to frame1
        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text="Programing is fun")
        self.lbl.pack()

        # add a label, entry, button, two radio buttons to frame2
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter text ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable=self.msg)
        bt_change_text = Button(frame2, text="Change text",
                                command=self.process_button)
        self.v1 = StringVar()
        rb_red = Radiobutton(frame2, text="Red", bg="red",
                             variable=self.v1, value='R',
                             command=self.process_radiobutton)
        rb_yellow = Radiobutton(frame2, text="Purple",
                                bg="purple", variable=self.v1, value='P',
                                command=self.process_radiobutton)

        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        bt_change_text.grid(row=1, column=3)
        rb_red.grid(row=1, column=4)
        rb_yellow.grid(row=1, column=5)

        window.mainloop()

    def process_radiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "red"
        elif self.v1.get() == 'P':
            self.lbl["fg"] = "purple"

    def process_button(self):
        self.lbl["text"] = self.msg.get()


ChangeLabelDemo()
