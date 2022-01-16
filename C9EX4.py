## Cap 9 - Lists
# EX 3 - Bounce balls

from tkinter import *
from random import randint


# Return a random color string in the form #RRGGBB
def get_random_color():
    color = "#"
    for j in range(6):
        color += to_hex_char(randint(0, 15))  # add a random digit
    return color


# convert an integer to a single hex digit in a character
def to_hex_char(hex_value):
    if 0 <= hex_value <= 9:
        return chr(hex_value + ord('0'))
    else:  # 10 <= hex_value <= 15
        return chr(hex_value - 10 + ord('A'))


# define a Ball class
class Ball:
    def __init__(self):
        self.x = 0  # starting center position
        self.y = 0
        self.dx = 2  # move right by default
        self.dy = 2  # move down by default
        self.radius = 3  # the radius is fixed
        self.color = get_random_color()


class BounceBalls:
    def __init__(self):
        self.ball_list = []

        window = Tk()
        window.title("Bouncing Balls")

        self.width = 350
        self.height = 150
        self.canvas = Canvas(window, bg="white",
                             width=self.width, height=self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        bt_stop = Button(frame, text="Stop", command=self.stop)
        bt_stop.pack(side=LEFT)
        bt_resume = Button(frame, text="Resume", command=self.resume)
        bt_resume.pack(side=LEFT)
        bt_add = Button(frame, text="+", command=self.add)
        bt_add.pack(side=LEFT)
        bt_remove = Button(frame, text="-", command=self.remove)
        bt_remove.pack(side=LEFT)

        self.sleep_time = 100
        self.is_stopped = False
        self.animate()

    def stop(self):
        self.is_stopped = True

    def resume(self):
        self.is_stopped = False
        self.animate()

    def add(self):  # add a new ball
        self.ball_list.append(Ball())

    def remove(self):
        self.ball_list.pop()

    def animate(self):
        while not self.is_stopped:
            self.canvas.after(self.sleep_time)
            self.canvas.update()
            self.canvas.delete("ball")

            for ball in self.ball_list:
                self.redisplay_ball(ball)

    def redisplay_ball(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx

        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius,
                                ball.y - ball.radius, ball.x + ball.radius,
                                ball.y + ball.radius, fill=ball.color, tags="ball")


BounceBalls()
