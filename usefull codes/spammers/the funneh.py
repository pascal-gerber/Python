from tkinter import *
import threading 
import os

def createLoop():
    window = Tk()
    funny = ""
    for i in range(100):
        funny += "im a virus im a virus im a virus im a virus im a virus im a virus im a virus \n"
    Button(window, text=funny, command=killpython, borderwidth=0).grid()
    window.geometry("500x500")
    window.title("im a virus")
    window.attributes('-topmost',True)
    window.mainloop()

def killpython():
    os._exit(0)


for each in range(100):
    annoying = threading.Thread(target=createLoop)
    annoying.start()  
