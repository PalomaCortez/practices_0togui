## Cap 8 - GUI
# Ex12 - Enlarge or Shrink Circle


from tkinter import *


class EnlargeShrinkCircle:
    def __init__(self):
        self.radius = 50

        window = Tk()
        window.title("Control Circle Demo")
        self.canvas = Canvas(window, bg="white", width=500, height=500)
        self.canvas.pack()
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius,
            100 + self.radius, 100 + self.radius, tags="oval")

        # bind canvas with a mouse events
        self.canvas.bind("<Button-1>", self.increase_circle)
        self.canvas.bind("<Button-3>", self.decrease_circle)

        window.mainloop()

    def increase_circle(self, event):
        self.canvas.delete("oval")
        if self.radius < 100:
            self.radius += 2
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius,
            100 + self.radius, 100 + self.radius, tags="oval")

    # display oval
    def decrease_circle(self, event):
        self.canvas.delete("oval")
        if self.radius > 2:
            self.radius -= 2
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius,
            100 + self.radius, 100 + self.radius, tags="oval")


EnlargeShrinkCircle()
