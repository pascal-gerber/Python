from tkinter import *


def doNothing():
    print("Test")


window = Tk()

options= Menu(window)
window.config(menu=options)

cascades=Menu(options,tearoff=False)
options.add_cascade(label="branches",menu= cascades)
cascades.add_command(label="first",command=doNothing)
cascades.add_command(label="second",command=doNothing)
cascades.add_command(label="thirth",command=doNothing)

options.add_command(label="test",command=doNothing)

window.geometry("500x500")
window.mainloop()
