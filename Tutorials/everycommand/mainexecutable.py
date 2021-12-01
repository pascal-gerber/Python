from tkinter import *
import subprocess
import os
import sys



def buildpath(filename):
    pathtofiles = ""
    droppedFile = sys.argv[0]
    droppedFile = droppedFile.split("\\")
    del droppedFile[-1]
    for each in droppedFile:
        pathtofiles += each + "\\"
    pathtofiles += filename
    subprocess.call(["C:\Python310\Lib\idlelib\idle.bat", pathtofiles])

def number(num):
    fileNames = ["Print.py", "variables1.py", "variables2.py", "variables3.py"]
    buildpath(fileNames[num])

def createinterface():
    window = Tk()
    titles = ["print explaination", "Variables part 1", "Variables part 2", "conversion of variables"]
    mylist = Listbox(window, yscrollcommand = Scrollbar.set)
    for easystages in range(len(titles)):
        easy = Button(window, text=titles[easystages], bg="Aqua",
                      command=lambda number = number, easystages = easystages:number(easystages),
                      height = 5, width = 15)
        easy.grid(row = int(easystages//4), column = easystages - (easystages//4))
    window.geometry("500x500")
    window.mainloop()
            
createinterface()
