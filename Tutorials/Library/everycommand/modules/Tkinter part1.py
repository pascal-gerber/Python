#tkinter is a very interesting part
#tkinter makes a gui "Grafical User Interface"
#there are multiples ways to import tkinter but i always recommand the all import
from tkinter import *
#this will import all of tkinter
#theres another but i don't like it that much, but its your choice

#import tkinter as Tk

#is the other one type of import
#the import all, will make the code shorter and easier to understand.

#first we have to create a window
window = Tk()
#already only this function will create a blank window.

#now there are multiple ways to add things into the window.
#the Label being a simple text
#it has to be defined on which window the label has to be at the start
Label(window, text="I am a simple label").grid()
#this is a very simple label

#before closing the window, you can mess around with the windows parameters
#first maybe the background color "it isn't essential, its just a extra touch"
window.configure(bg = "Blue")

#there are 2 extra touch which whould be very usefull
window.geometry("500x500")
#i recommand to add 500x500 since its a good size
#the x is a simple X letter.

#and the title
window.title("guide 1")

#now to close the window, you have to make it a mainloop.
window.mainloop()

#of course there are other objects you can add to the window
#but that will be for another file
