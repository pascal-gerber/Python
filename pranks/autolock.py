import keyboard
import subprocess
import time
import threading
import os
from tkinter import *

def Lockme():
    time.sleep(3)
    cmd='rundll32.exe user32.dll, LockWorkStation'
    subprocess.call(cmd)

def killpython():
    os._exit(0)

def nonowindow():
    window = Tk()
    Label(window, height=10, width=10).grid(row=1, column=1) 
    remove = Button(window, text="Please do not touch", command=killpython, height=10, width=50, borderwidth=0)
    remove.grid(row=2, column=2)
    window.geometry("500x500")
    window.attributes('-topmost',True)
    window.title("Okay bye")
    window.mainloop()

def lockedState():
    second = Tk()
    Label(second, height=10, width=10).grid(row=1, column=1)
    Label(second, text="currently away!!").grid(row=2, column=2)
    second.geometry("500x500")
    second.attributes('-topmost',True)
    second.title("AFK")
    second.mainloop()

thirth = threading.Thread(target=lockedState)
thirth.start()

keyboard.read_key()
first = threading.Thread(target=nonowindow)
second = threading.Thread(target=Lockme)

first.start()
second.start()






