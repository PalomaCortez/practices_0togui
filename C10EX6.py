## C10 Inheritance and Polymorphism
# EX6 Display clock

from tkinter import *
from C10EX7 import StillClock


class DisplayClock:
    def __init__(self):
        window = Tk()
        window.title("Change clock time")

        self.clock = StillClock(window)
        self.clock.pack()

        frame = Frame(window)
        frame.pack()
        Label(frame, text="Hour: ").pack(side=LEFT)
        self.hour = IntVar()
        self.hour.set(self.clock.get_hour())
        Entry(frame, textvariable=self.hour,
              width=2).pack(side=LEFT)
        Label(frame, text="Minute: ").pack(side=LEFT)
        self.minute = IntVar()
        self.minute.set(self.clock.get_minute())
        Entry(frame, textvariable=self.minute,
              width=2).pack(side=LEFT)
        Label(frame, text="Second: ").pack(side=LEFT)
        self.second = IntVar()
        self.second.set(self.clock.get_second())
        Entry(frame, textvariable=self.second,
              width=2).pack(side=LEFT)
        Button(frame, text="Set new time",
               command=self.set_new_time).pack(side=LEFT)
        window.mainloop()

    def set_new_time(self):
        self.clock.set_hour(self.hour.get())
        self.clock.set_minute(self.minute.get())
        self.clock.set_second(self.second.get())


DisplayClock()
