## Cap 8 - GUI
# EX7 - Image Demo

from tkinter import *


class ImageDemo:
    def __init__(self):
        window = Tk()
        window.title("Image Demo")

        # create PhotoImage objects
        ca_image = PhotoImage(file="image/ca.gif")
        china_image = PhotoImage(file="image/china.gif")
        left_image = PhotoImage(file="image/left.gif")
        right_image = PhotoImage(file="image/right.gif")
        us_image = PhotoImage(file="image/usIcon.png")
        uk_image = PhotoImage(file="image/ukIcon.png")
        cross_image = PhotoImage(file="image/x.png")
        circle_image = PhotoImage(file="image/o.png")

        # Frame1 to contain label and canvas
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image=ca_image).pack(side=LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image=china_image)
        canvas["width"] = 200
        canvas["height"] = 100
        canvas.pack(side=LEFT)

        # Frame 2 contains buttons, check buttons, nd radio buttons
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image=left_image).pack(side=LEFT)
        Button(frame2, image=right_image).pack(side=LEFT)
        Checkbutton(frame2, image=us_image).pack(side=LEFT)
        Checkbutton(frame2, image=uk_image).pack(side=LEFT)
        Radiobutton(frame2, image=cross_image).pack(side=LEFT)
        Radiobutton(frame2, image=circle_image).pack(side=LEFT)

        window.mainloop()


ImageDemo()
