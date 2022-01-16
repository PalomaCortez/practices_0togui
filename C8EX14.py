## Cap 8 - GUI
# Ex14 - Control Animation demo

from tkinter import *


class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("Control Animation Demo")

        self.width = 250  # width of the canvas
        self.canvas = Canvas(window, bg="white",
                             width=250, height=50)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        bt_stop = Button(frame, text="Stop", command=self.stop)
        bt_stop.pack(side=LEFT)
        bt_resume = Button(frame, text="Resume", command=self.resume)
        bt_resume.pack(side=LEFT)
        bt_faster = Button(frame, text="Faster", command=self.faster)
        bt_faster.pack(side=LEFT)
        bt_slower = Button(frame, text="Slower", command=self.slower)
        bt_slower.pack(side=LEFT)

        self.x = 0  # starting position
        self.sleep_time = 100
        self.canvas.create_text(self.x, 30,
                           text="Message moving?", tags="text")
        self.dx = 3
        self.is_stopped = False
        self.animate()

        window.mainloop()

    def stop(self):
        self.is_stopped = True

    def resume(self):
        self.is_stopped = False
        self.animate()

    def faster(self):
        if self.sleep_time > 5:
            self.sleep_time -= 20

    def slower(self):
        if self.sleep_time < 300:
            self.sleep_time += 20

    def animate(self):
        while not self.is_stopped:
            self.canvas.move("text", self.dx, 0)  # move text
            self.canvas.after(self.sleep_time)  # sleep for 100 milliseconds
            self.canvas.update()
            if self.x < self.width:
                self.x += self.dx
            else:
                self.x = 0  # reset string position to the beginning
                self.canvas.delete("text")
                # redraw text at the beginning
                self.canvas.create_text(self.x, 30, text="message moving?", tags="text")


ControlAnimation()
