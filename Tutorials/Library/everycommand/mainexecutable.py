from tkinter import *
from tkinter import filedialog
import subprocess
import os
import sys
import csv
import getpass
import pathlib
import threading
import webbrowser

################################################################################################################
#for easier purposes of editing the file, i put all the changable needed variable lists on the top.
#these are the filenames choosen from python from specific paths
easystages = ["Print.py", "variables1.py", "variables2.py", "variables3.py", "Variable changes 1.py",
                     "List options.py","Input.py", "If function.py", "Loops.py", "functions.py",
                     "String options.py", "Math module and calculations.py", "indexes.py"
                     ]

mediumstages = ["classes.py", "open.py", "String Manipulation.py"]

hardstages = ["Encapsulation.py"]

modulestages = ["Modules.py","Timemodule.py", "Turtle.py",  "osmodule.py", "Tkinter part1.py", "Tkinter part2.py",
                "Tkinter part3.py", "Tkinter part4.py", "Sys.py"]

projectstages = ["turtlestar.py", "goatgame.py", "Clock.py"]

bonusstages = ["Lists.py", "Editing files.py"]

################################################################################################################
#same reason here why its on the top
#but these are the visual titles on the pages
easytitles = ["print explaination", "Variables part 1", "Variables part 2", "conversion of\nvariables", "string and lists",
              "List sorting", "input", "if function", "python loops", "Functions", 
              "string options", "Mathematical\noperations","List Indexes"]

mediumtitles = ["classes", "edit files", "string manipulation"]

hardtitles = ["Encapsulation\nprivate class"]

moduletitles = ["download\nmodules","time module", "basic Turtle", "os module", "Gui part 1", "Gui part 2",
                "Gui part 3", "Gui part 4", "system - sys"]

projecttitles = ["Turtle star", "Goat game", "Clock to 2030"]

bonustitles = ["Lists", "File manipulation"]
################################################################################################################

#these are the colors of each section
#"can be edited if colors don't fit your needs"
#_______________________________________________________________________________________
easycol = ["DarkTurquoise", "Aqua"]
mediumcol = ["LimeGreen", "Lime"]
hardcol = ["FireBrick", "Red"]
modulecol = ["Teal", "LightSeaGreen"]
projectcol = ["Gold", "Yellow"]
bonuscol = ["Silver", "Gainsboro"]
#_______________________________________________________________________________________

#some variable lines "should not be edited"
Diffcolors = [easycol, mediumcol, hardcol, modulecol, projectcol, bonuscol]
difficulties = ["easy", "medium", "hard", "modules", "projects", "Bonus codes"]
ObjList = []
filename = ""



##################################################################################################################
##################################################################################################################
#______________________________Android_Usability_________________________________________________________________#
##################################################################################################################
##################################################################################################################

editClick = ""
editVal = None
showCode = None

#android specific kill window
def killwindow(Object):
    Object.destroy()

#very very confusing why tkinter is the only module on android that can copy to clipboard
#but as long as it works... i guess...
def androidcopytoclipboard(filetext, newWindow):
    copyandroid = Tk()
    copyandroid.withdraw()
    copyandroid.clipboard_clear()
    copid = Label(newWindow, text="content has been copied\nto clipboard\nnote: exiting the programm will empty\n" +
                  "your clipboard.")
    copid.grid(row=3)
    copyandroid.clipboard_append(filetext)

#edit localfile
def switchedit(switch):
    global showCode
    global editVal
    global editClick
    if editVal == False:
        editVal = True
        showCode['state'] = NORMAL
        editClick.configure(text="Edit :" + str(editVal))
    elif editVal == True:
        editVal = False
        showCode['state'] = DISABLED
        editClick.configure(text="Edit :" + str(editVal))

#android use
def android(pathfile):
    global showCode
    global editClick
    global editVal
    global openname
    newWindow = Tk()
    newWindow.configure(bg="Grey")
    readedcontent = ""
    with open(pathfile) as f:
        for line in csv.reader(f):
            try:
                allcontent = ",".join(line)
                readedcontent += (str(allcontent) + "\n")
            except:
                readedcontent += "\n"
        content = (readedcontent)
    showCode = Text(newWindow,height = 20)
    showCode.grid(columnspan=3)
    showCode.insert('1.0', content)
    showCode['state'] = DISABLED
    editVal = False
    editClick = Button(newWindow, text="Edit :" + str(editVal),
                       command=lambda showCode = showCode: switchedit(showCode),
                       height = 5, width = 15)
    editClick.grid(row=2, column=0)
    copytoClip = Button(newWindow, text="copy whole text\n to keyboard",
                        command=lambda newWindow = newWindow,
                        showCode = showCode:androidcopytoclipboard(str(showCode.get("1.0", END)), newWindow),
                        height = 5, width = 15)
    copytoClip.grid(row=2, column=1)
    leave = Button(newWindow, text="exit viewer", command=lambda newWindow = newWindow:killwindow(newWindow),
                   height = 5, width = 15)
    leave.grid(row=2, column=2)
    newWindow.title(openname)
    newWindow.mainloop()

openname = ""

#this selects files from the library
def buildpath(filename, difficulty):
    global openname
    openname = filename
    pathtofiles = ""
    if sys.platform == "win32" or sys.platform == "win64":
        droppedFile = os.getcwd()
        lines = "\\"
    elif sys.platform == "linux":
        droppedFile = pathlib.Path(__file__).parent.resolve()
        lines = "/"
    if difficulty == "easy":
        pathtofiles += "easy" + lines + filename
    elif difficulty == "medium":
        pathtofiles += "medium" + lines + filename
    elif difficulty == "hard":
        pathtofiles += "hard" + lines + filename
    elif difficulty == "modules":
        pathtofiles += "modules" + lines + filename
    elif difficulty == "projects":
        pathtofiles += "projects" + lines + filename
    elif difficulty == "Bonus codes":
        pathtofiles += "Bonus" + lines + filename

    pathtofiles = str(droppedFile) + lines + pathtofiles
    #for other platforms \/
    if sys.platform == "win32" or sys.platform == "win64":
        openpython(pathtofiles)
    elif sys.platform == "linux":
        android(pathtofiles)

##################################################################################################################
##################################################################################################################

#this opens the requested file with the python program.
def openpython(path):
    global filename
    if len(filename) > 0:
        subprocess.call([filename, path])
    else:    
        exists = False
        for i in reversed(range(11)):
            try:
                subprocess.call(["C:\Program Files\Python3" + str(i) + "\Lib\idlelib\idle.bat", path])
                exists = True
                break
            except:
                pass
        if exists == False:
            for i in reversed(range(11)):
                try:
                    subprocess.call(["C:\Python3" + str(i) + "\Lib\idlelib\idle.bat", path])
                    exists = True
                    break
                except:
                    pass
            if exists == False:
                for i in reversed(range(11)):
                    pathtopython = (str("C:\\Users\\" + getpass.getuser() + "\AppData\Local\Programs\Python\Python3") + str(i) + str("\Lib\idlelib\idle.bat"))
                    try:
                        subprocess.call([pathtopython, path])
                        exists = True
                        break
                    except:
                        pass
                if exists == False:
                    information = Tk()
                    Label(information, text="Choose the Idle.bat file to start files over the path")
                    filename = filedialog.askopenfilename(initialdir = "/",
                                                          title = "Idle.bat",
                                                          filetypes = (("Text files", "*.bat*"), ("all files","*.*")))
                    exists = True
                    subprocess.call([filename, path])
                    information.mainloop()

        

def number(num, difficulty):
    global easystages
    global mediumstages
    global hardstages
    global modulestages
    global projectstages
    global bonusstages
        #_______________________________________Specific Button selector_________________________________
        ########################################Easy#####################################################
    if difficulty == "easy":
                buildpath(easystages[num], "easy")
        ########################################Medium#####################################################
    elif difficulty == "medium":
        buildpath(mediumstages[num], "medium")
        ########################################Hard#####################################################
    elif difficulty == "hard":
        buildpath(hardstages[num], "hard")
        ########################################Modules#####################################################
    elif difficulty == "modules":
        buildpath(modulestages[num], "modules")
        ########################################projects#####################################################
    elif difficulty == "projects":
        buildpath(projectstages[num], "projects")
        ########################################Bonus codes#####################################################
    elif difficulty == "Bonus codes":
        buildpath(bonusstages[num], "Bonus codes")
        
def destroyLabel():
    global ObjList
    for Obj in ObjList:
        Obj.destroy()
    ObjList = []
#_______________________________________Easy_____________________________________________________        
########################################Easy#####################################################
#there are all the settups for each page

#font for each    
titlefont = ("Bahnschrift", 11)
    
def easySetup():
    global ObjList
    global window

    window.configure(bg=easycol[0])
    titles = easytitles
    
    easytext = Label(window, text="Basic simple knowledge", height = 5, width=65, bg=easycol[0], font = titlefont)
    easytext.grid(row=1, column=0, columnspan=6)
    ObjList.append(easytext)
    for easystages in range(len(titles)):
        easy = Button(window, text=titles[easystages], bg=easycol[1],
                      command=lambda number = number, easystages = easystages:number(easystages, "easy"),
                      height = 5, width = 15)
        easy.grid(row = (int(easystages//4)) + 2, column = easystages - (easystages//4)*4)
        ObjList.append(easy)
#_______________________________________Medium_____________________________________________________
########################################Medium#####################################################
        
def mediumSetup():
    window.configure(bg=mediumcol[0])
    titles = mediumtitles

    mediumtext = Label(window, text="Basic Highter knowledge", height = 5, width=65, bg=mediumcol[0], font = titlefont)
    mediumtext.grid(row=1, column=0, columnspan=6)
    ObjList.append(mediumtext)
    for mediumstages in range(len(titles)):
        medium = Button(window, text=titles[mediumstages], bg=mediumcol[1],
                      command=lambda number = number, mediumstages = mediumstages:number(mediumstages, "medium"),
                      height = 5, width = 15)
        medium.grid(row = (int(mediumstages//4)) + 2, column = mediumstages - (mediumstages//4)*4)
        ObjList.append(medium)
#_______________________________________Hard_____________________________________________________
########################################Hard#####################################################
        
def hardSetup():
    window.configure(bg=hardcol[0])
    titles = hardtitles

    hardtext = Label(window, text="Advanced knowledge", height = 5, width=65, bg=hardcol[0], font = titlefont)
    hardtext.grid(row=1, column=0, columnspan=6)
    ObjList.append(hardtext)
    for hardstages in range(len(titles)):
        hard = Button(window, text=titles[hardstages], bg=hardcol[1],
                      command=lambda number = number, hardstages = hardstages:number(hardstages, "hard"),
                      height = 5, width = 15)
        hard.grid(row = (int(hardstages//4)) + 2, column = hardstages - (hardstages//4)*4)
        ObjList.append(hard)
#_______________________________________modules_____________________________________________________
########################################modules#####################################################
        
def moduleSetup():
    window.configure(bg=modulecol[0])
    titles = moduletitles
    regexButton = Button(window, text="Regex", command = regexSetup, width = 30, height = 5, bg="grey")
    regexButton.grid(row = 0, column = 1, columnspan = 2)
    ObjList.append(regexButton)
    moduletext = Label(window, text="Modules", height = 5, width=65, bg=modulecol[0], font = titlefont)
    moduletext.grid(row=1, column=0, columnspan=6)
    ObjList.append(moduletext)
    for modulestages in range(len(titles)):
        module = Button(window, text=titles[modulestages], bg=modulecol[1],
                      command=lambda number = number, modulestages = modulestages:number(modulestages, "modules"),
                      height = 5, width = 15)
        module.grid(row = (int(modulestages//4)) + 2, column = modulestages - (modulestages//4)*4)
        ObjList.append(module)
#_______________________________________projects_____________________________________________________
########################################projects#####################################################
        
def projectSetup():
    window.configure(bg=projectcol[0])
    titles = projecttitles

    projecttext = Label(window, text="Projects", height = 5, width=65, bg=projectcol[0], font = titlefont)
    projecttext.grid(row=1, column=0, columnspan=6)
    ObjList.append(projecttext)
    for projectstages in range(len(titles)):
        project = Button(window, text=titles[projectstages], bg=projectcol[1],
                      command=lambda number = number, projectstages = projectstages:number(projectstages, "projects"),
                      height = 5, width = 15)
        project.grid(row = (int(projectstages//4)) + 2, column = projectstages - (projectstages//4)*4)
        ObjList.append(project)
#______________________________________Bonus codes______________________________________________________    
########################################Bonus codes#####################################################
        
def bonusSetup():
    window.configure(bg=bonuscol[0])
    titles = bonustitles

    bonustext = Label(window, text="Bonuses and shortcuts\nLife hacks", height = 5, width=65, bg=bonuscol[0], font = titlefont)
    bonustext.grid(row=1, column=0, columnspan=5)
    ObjList.append(bonustext)
    for bonusstages in range(len(titles)):
        bonus = Button(window, text=titles[bonusstages], bg=bonuscol[1],
                      command=lambda number = number, bonusstages = bonusstages:number(bonusstages, "Bonus codes"),
                      height = 5, width = 15)
        bonus.grid(row = (int(bonusstages//4)) + 2, column = bonusstages - (bonusstages//4)*4)
        ObjList.append(bonus)

#_________________________________Tutorial for regex______________________________________________________
##########################################################################################################


def regexSetup():
    Regex = Tk()

#######################################Information############################################################
    
    Information = Label(Regex, text="regex is a Module that finds\nspecific pattern into the text", bg="BurlyWood")
    Information.grid(row=1, column=1, columnspan=4)

    helptext = ("Cheatset:\n[aeoiu] *finds all the vovels in the text\n" +
                "(hello) *finds the specific words 'hello'\n" +
                "[^aeiou] *excludes all vowels\n\nNow the signs after those blocks\n" +
                "*  will select everything correct and connect them all\n" +
                "+  same but only works for one or more than one\n" +
                "?  will only select one at a time and ignore the empty\n" +
                "{2} will select 2 correct at a time\n\n" +
                "at the end a code will look like that:\n" +
                "[aeiou]*(hello){2}\n\nhere are some links:")

#########################################Buttons########################################################

    cheatSet = Label(Regex, text=helptext, bg="BurlyWood")
    cheatSet.grid(row=2, column=1, columnspan=4)

    FirstRegex = Button(Regex, text="regex101", command=lambda openLink = openLink:openLink("https://regex101.com/"),
                        height=10, width=15, bg="Moccasin")
    FirstRegex.grid(row=3, column=1)
    SecondRegex = Button(Regex, text="regexr", command=lambda openLink = openLink:openLink("https://regexr.com/"),
                         height=10, width=15, bg="Moccasin")
    SecondRegex.grid(row=3, column=2)
    cheatsheet = Button(Regex, text="Cheatsheet 1", command=lambda openLink = openLink:openLink("https://medium.com/factory-mind/regex-cookbook-most-wanted-regex-aa721558c3c1"),
                        height=10, width=15, bg="Moccasin")
    cheatsheet.grid(row=3, column=3)
    secondCheat = Button(Regex, text="Cheatsheet 2", command=lambda openLink = openLink:openLink("https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html"),
                         height=10, width=15, bg="Moccasin")
    secondCheat.grid(row=3, column=4)
    pythonRegex = Button(Regex, text="python", command=showpyhton,
                         height=10, width=15, bg="Moccasin")
    pythonRegex.grid(row=3, column=5) 

    Regex.configure(bg="BurlyWood")
    if sys.platform == "win32" or sys.platform == "win64":
        Regex.geometry("600x500")
    elif sys.platform == "linux":
        Regex.geometry("2000x1000")
    Regex.title("Regex")
    Regex.mainloop()


##########################################################################################################
    
def openLink(link):
    webbrowser.open_new(link)
##########################################################################################################
    
def showpyhton():
    if sys.platform == "win32" or sys.platform == "win64":
        droppedFile = os.getcwd()
        lines = "\\"
    elif sys.platform == "linux":
        droppedFile = pathlib.Path(__file__).parent.resolve()
        lines = "/"
        
    pathtofiles = str(droppedFile) + lines + "regex" + lines + "Regex.py"

    if sys.platform == "win32" or sys.platform == "win64":
        openpython(pathtofiles)
    elif sys.platform == "linux":
        android(pathtofiles)

#__________________________________Pages___________________________________________________________________
###########################################################################################################

def switch(Name):
    global ObjList
    global DifficultyUp
    global DifficultyDown
    destroyLabel()

    Number = difficulties.index(Name)
    oneUp = Number + 1
    oneDown = Number - 1
    if oneUp == 6:
        oneUp = 0
    if oneDown == -1:
        oneDown = 5
        
    DifficultyUp.configure(text=difficulties[oneUp],bg = Diffcolors[oneUp][0],
                           command=lambda difficulties = difficulties:switch(difficulties[oneUp]))
    DifficultyDown.configure(text=difficulties[oneDown], bg = Diffcolors[oneDown][0],
                             command=lambda difficulties = difficulties:switch(difficulties[oneDown]))
    if Name == "easy":
        easySetup()
    elif Name == "medium":
        mediumSetup()
    elif Name == "hard":
        hardSetup()
    elif Name == "modules":
        moduleSetup()
    elif Name == "projects":
        projectSetup()
    elif Name == "Bonus codes":
        bonusSetup()
#__________________________________________swap pages function_____________________________________________
###########################################################################################################

def difficultyswitch():
    global window
    global DifficultyUp
    global DifficultyDown
    DifficultyUp = Button(window, text=difficulties[1],
                          command=lambda difficulties = difficulties:switch(difficulties[1]), width = 15, height = 5,
                          bg = Diffcolors[1][0])
    DifficultyUp.grid(row = 0, column = 3)
    DifficultyDown = Button(window, text=difficulties[5],
                            command=lambda difficulties = difficulties:switch(difficulties[5]), width = 15, height = 5,
                            bg = Diffcolors[5][0])
    DifficultyDown.grid(row = 0, column = 0)
#_________________________________button changer___________________________________________________________
###########################################################################################################

def createinterface():
    global window
    window = Tk()
    easySetup()
    difficultyswitch()
    window.title("python library")
    window.geometry("500x600")
    window.mainloop()
            
createinterface()
