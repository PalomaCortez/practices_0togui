## Cap 8 - GUI
# Ex11 - Mouse Key Event demo


from tkinter import *


class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("Event Demo")
        canvas = Canvas(window, bg="white", width=200, height=100)
        canvas.pack()

        # bind with a <Button-1> event
        canvas.bind("<Button-1>", self.process_mouse_event)

        # bind with <key> event
        canvas.bind("<Key>", self.process_key_event)
        canvas.focus_set()

        window.mainloop()

    def process_mouse_event(self, event):
        print("clicked at", event.x, event.y)
        print("position in the screen", event.x_root, event.y_root)
        print("which button is clicked", event.num)

    # display oval
    def process_key_event(self, event):
        print("keysym? ", event.keysym)
        print("char? ", event.char)
        print("keycode? ", event.keycode)


MouseKeyEventDemo()
