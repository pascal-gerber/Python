from tkinter import *
#as usual the import

#usual guides use root or master
#its easier if its simply called a window
window = Tk()

#now for each object there are a lot of different customisations and ways to write
changableLabel = Label(window, text="click the button i change", height=10, width=20, bg="Green")
#to be able to change options in the object putting ".grid()" at the end can cause issues
changableLabel.grid()
#this is a way better way to write stuff

#now we need a function and a button since buttons can only activate functions
def clicked():
    #with configure, you can change any option in the object.
    changableLabel.configure(text="i have changed", bg="Red")

#now the button
     #button \/                                 the command  \/
clickMe = Button(window, text="i change the label", command=clicked)
clickMe.grid(row = 2)
#theres .pack() as well, but i recommand always using grid
#in grid you can put it at a specific place

#if theres an object with ".pack" the geometry function will not work.
#which is why i always recommand grid, and on grid you can change the
#positionning.
window.geometry("500x500")
window.title("guide 2")
window.mainloop()
