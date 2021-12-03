from tkinter import *
import subprocess
import os
import sys



def buildpath(filename):
    global pathtofiles
    pathtofiles = ""
    droppedFile = sys.argv[0]
    droppedFile = droppedFile.split("\\")
    del droppedFile[-1]
    for each in droppedFile:
        pathtofiles += each + "\\"
    pathtofiles += filename
    openpython()

def openpython():
    global pathtofiles
    exists = False
    for i in reversed(range(11)):
        try:
            subprocess.call(["C:\Python3" + str(i) + "\Lib\idlelib\idle.bat", pathtofiles])
            exists = True
            break
        except:
            pass
    if exists == False:
        newWindow = Tk()
        Label(newWindow, text="you do not have idle.\n you should try to download idle").grid(rowspan=3)
        Button(newWindow, text="download\nidle", command=openbrowser, width=10, height=5).grid()
        newWindow.geometry("300x300")
        newWindow.title("install idle")
        newWindow.mainloop()
            

def openbrowser():
    import webbrowser
    webbrowser.open("https://www.python.org/downloads/release/python-3100/", new=0, autoraise=True)

def number(num):
    fileNames = ["Print.py", "variables1.py", "variables2.py", "variables3.py", "Variable changes 1.py",
                 "List options.py", "If function.py", "Loops.py"]
    buildpath(fileNames[num])

def createinterface():
    window = Tk()
    titles = ["print explaination", "Variables part 1", "Variables part 2", "conversion of\nvariables", "string and lists",
              "List sorting", "if function", "python loops"]
    mylist = Listbox(window, yscrollcommand = Scrollbar.set)
    for easystages in range(len(titles)):
        easy = Button(window, text=titles[easystages], bg="Aqua",
                      command=lambda number = number, easystages = easystages:number(easystages),
                      height = 5, width = 15)
        easy.grid(row = int(easystages//4), column = easystages - (easystages//4)*4)
    window.geometry("500x500")
    window.mainloop()
            
createinterface()
