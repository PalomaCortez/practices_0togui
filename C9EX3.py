## Cap 9 - Lists
# EX 3 - Deck of cards with GUI

from tkinter import *
import random

class DeckOfCardsGUI:
    def __init__(self):
        window = Tk()
        window.title("Pick four cards randomly")

        self.image_list = []  # store image for cards
        for i in range(1, 53):
            self.image_list.append(PhotoImage(file="image/"
                                                   + str(i) + ".gif"))

        frame = Frame(window)  # hold four labels for cards
        frame.pack()

        self.label_list = []  # a list of four labels
        for i in range(4):
            self.label_list.append(Label(frame,
                                         image=self.image_list[i]))
            self.label_list[i].pack(side=LEFT)

        Button(window, text="Shuffle",
               command=self.shuffle).pack()

        window.mainloop()

    # choose four random cards
    def shuffle(self):
        random.shuffle(self.image_list)
        for i in range(4):
            self.label_list[i]["image"] = self.image_list[i]

DeckOfCardsGUI()
