#this is how i recommand to install tkinter
#i dont recommand "import tkinter as Tk" or simply "import tkinter".
from tkinter import *

#i rather call it "window" than "root" or "main" since it describes it best.
#a Tk() object is the window itself, its empty and seen as a variable type
window = Tk()

#And heres a simple label showing the type of the window
#i recommand for texts that should change to add a variable
windowtype = Label(window, text=str(type(window)))
#i also recommand to set the "grid" or "pack" to another line since it will prevent some certain bugs from occuring
windowtype.grid(row = 1, column = 1)
#recommanding the "grid" over the "pack" since you got "row" and "column" you can define

#this is the size of the window, i recommand 500x500, the "x" is basicly just the letter X.
window.geometry("500x500")

#this is the name of the window that appears on the GUI
window.title("type of window")

#the mainloop is needed so it can be executed outside of the editor
window.mainloop()
