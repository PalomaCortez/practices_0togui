## Cap 8 - GUI
# Ex15 - Dialog demo

import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

# the messagebos icons can be different on apple/windows
tkinter.messagebox.showinfo("showinfo", "This is an info msg")

tkinter.messagebox.showwarning("showwarning", "This is a warning")

tkinter.messagebox.showerror("showerror", "This is an error")

is_yes = tkinter.messagebox.askyesno("askyesno", "Continue?")
print(is_yes)

is_ok = tkinter.messagebox.askokcancel("askokcancel", "OK?")
print(is_ok)

is_yes_no_cancel = tkinter.messagebox.askyesnocancel(
    "askyesnocancel", "Yes, no, cancel?")
print(is_yes_no_cancel)

name = tkinter.simpledialog.askstring(
    "askstring", "Enter your name")
print(name)

age = tkinter.simpledialog.askinteger("askinteger", "Enter your age")
print(age)

weight = tkinter.simpledialog.askfloat("askfloat", "Enter your weight")
print(weight)
