## Cap 8 - GUI
# EX5 - Canvas Demo

from tkinter import *


class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")

        self.canvas = Canvas(window, width=200, height=100,
                             bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        bt_rectangle = Button(frame, text="Rectangle",
                              command=self.display_rect)
        bt_oval = Button(frame, text="Oval",
                         command=self.display_oval)
        bt_arc = Button(frame, text="Arc",
                        command=self.display_arc)
        bt_polygon = Button(frame, text="Polygon",
                            command=self.display_polygon)
        bt_line = Button(frame, text="Line",
                         command=self.display_line)
        bt_string = Button(frame, text="String",
                           command=self.display_string)
        bt_clear = Button(frame, text="Clear",
                          command=self.clear_canvas)

        bt_rectangle.grid(row=1, column=1)
        bt_oval.grid(row=1, column=2)
        bt_arc.grid(row=1, column=3)
        bt_polygon.grid(row=1, column=4)
        bt_line.grid(row=1, column=5)
        bt_string.grid(row=1, column=6)
        bt_clear.grid(row=1, column=7)

        window.mainloop()

    def display_rect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def display_oval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    def display_arc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0,
                               extent=90, width=0, fill="purple", tags="arc")

    def display_polygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50,
                                   tags="polygon")

    def display_line(self):
        self.canvas.create_line(10, 10, 190, 90, fill="green",
                                tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9,
                                arrow="last", activefill="blue", tags="line")

    def display_string(self):
        self.canvas.create_text(60, 40, text="Hi, I am a string",
                                font="times 10 bold underline", tags="string")

    def clear_canvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon",
                           "line", "string")

CanvasDemo()
