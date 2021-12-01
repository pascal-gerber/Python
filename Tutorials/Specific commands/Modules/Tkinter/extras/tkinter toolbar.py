from tkinter import *
#import sys


def doNothing():
    print("Test")


window = Tk()
Toolbar = Menu(window)
window.config(menu=Toolbar)

option1 = Menu(Toolbar)
Toolbar.add_cascade(label="Test1", menu=option1)
Toolbar.add_command(label="Click", command = doNothing)

window.mainloop()
