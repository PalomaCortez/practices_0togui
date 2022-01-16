## C11 Files and Exception Handling       file with png does not work
# Ex6 Edit files
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple text editor")

        # Create a menu bar
        menubar = Menu(window)
        window.config(menu=menubar)  # display the menu bar

        # Create a pull-down menu and add it to the menu bar
        operation_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=operation_menu)
        operation_menu.add_command(label="Open",
                                   command=self.open_file)
        operation_menu.add_command(label="Save",
                                   command=self.save_file)

        # add a toolbar frame
        frame0 = Frame(window)
        frame0.grid(row=1, column=1, sticky=W)

        # create images
        # open_image = PhotoImage(file="image/open.png")
        # save_image = PhotoImage(file="image/save.png")

        # Button(frame0, image=open_image, command=
        #         self.open_file).grid(row=1, column=1, sticky=W)
        # Button(frame0, image=save_image,
        #        command=self.save_file).grid(row=1, column=2)

        Button(frame0, command=self.open_file).grid(row=1, column=1, sticky=W)
        Button(frame0, command=self.save_file).grid(row=1, column=2)

        frame1 = Frame(window)  # hold editor pane
        frame1.grid(row=2, column=1)

        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(frame1, width=40, height=20,
                         wrap=WORD, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)

        window.mainloop()

    def open_file(self):
        file_name_for_reading = askopenfilename()
        infile = open(file_name_for_reading, "r")
        self.text.insert(END, infile.read())  # read all from the file
        infile.close()

    def save_file(self):
        file_name_for_writting = asksaveasfilename()
        outfile = (open(file_name_for_writting, "w"))
        outfile.write(self.text.get(1.0, END))
        outfile.close()


FileEditor()
