## Cap 8 - GUI
# Ex13 - Animation demo

from tkinter import *


class AnimationDemo:
    def __init__(self):
        window = Tk()
        window.title("Animation Demo")

        width = 250  # width of the canvas
        canvas = Canvas(window, bg="white",
                             width=250, height=50)
        canvas.pack()

        x = 0  # starting position
        canvas.create_text(x, 30,
                           text="Message moving?", tags="text")
        dx = 3
        while True:
            canvas.move("text", dx, 0)  # move the text dx unit
            canvas.after(100)  # sleep for 100 milliseconds
            canvas.update()
            if x < width:
                x += dx
            else:
                x = 0  # reset string position to the beginning
                canvas.delete("text")
                # redraw text at the beginning
                canvas.create_text(x, 30, text="message moving?", tags="text")

        window.mainloop()


AnimationDemo()
