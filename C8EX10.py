## Cap 8 - GUI
# EX7 - Popup Menus


from tkinter import *


class PopupMenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Popup Menu Demo")

        # create a new menu bar
        menu_bar = Menu(window)
        window.config(menu=menu_bar)  # display the menu bar

        # Create a popup menu
        self.menu = Menu(menu_bar, tearoff=0)
        self.menu.add_command(label="Draw a line",
                              command=self.display_line)
        self.menu.add_command(label="Draw an oval",
                              command=self.display_oval)
        self.menu.add_command(label="Draw a rectangle",
                              command=self.display_rect)
        self.menu.add_command(label="Clear",
                              command=self.clear_canvas)

        # add a tool bar frame
        frame0 = Frame(window)
        frame0.grid(row=1, column=1, sticky=W)

        # Place canvas in window
        self.canvas = Canvas(window, width=200,
                             height=100, bg="white")
        self.canvas.pack()

        # bind popup to canvas
        self.canvas.bind("<Button-1>", self.popup)  # Button-3 for right click on mouse.

        window.mainloop()

    # display two lines
    def display_line(self):
        self.canvas.create_line(10, 10, 190, 90, tags="line")
        self.canvas.create_line(10, 90, 190, 90, tags="line")

    # display oval
    def display_oval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags="oval")

    # display a rectangle
    def display_rect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    # clear drawings
    def clear_canvas(self):
        self.canvas.delete("line", "oval", "rect")

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)


PopupMenuDemo()
