from tkinter import *


#Main command to make an object on a window draggable "all 3 commands do it"
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


window = Tk()

notes = Entry(window)
notes.pack()
make_draggable(notes)

text = Button(window, text="test")
text.pack()
make_draggable(text)

window.mainloop()
