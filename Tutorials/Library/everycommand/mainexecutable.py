from tkinter import *
from tkinter import filedialog
import subprocess
import os
import sys
import getpass

################################################################################################################
#for easier purposes of editing the file, i put all the changable needed variable lists on the top.
#these are the filenames choosen from python from specific paths
easystages = ["Print.py", "variables1.py", "variables2.py", "variables3.py", "Variable changes 1.py",
                     "List options.py","Input.py", "If function.py", "Loops.py", "functions.py",
                     "String options.py", "Math module and calculations.py", "indexes.py"
                     ]

mediumstages = ["classes.py", ""]

hardstages = [""]

modulestages = ["Modules.py","Timemodule.py", "Turtle.py",  "osmodule.py", "Tkinter part1.py", "Tkinter part2.py",
                "Tkinter part3.py", "Tkinter part4.py"]

projectstages = ["turtlestar.py"]

bonusstages = [""]

################################################################################################################
#same reason here why its on the top
#but these are the visual titles on the pages
easytitles = ["print explaination", "Variables part 1", "Variables part 2", "conversion of\nvariables", "string and lists",
              "List sorting", "input", "if function", "python loops", "Functions", 
              "string options", "Mathematical\noperations","List Indexes"]

mediumtitles = ["classes", ""]

hardtitles = [""]

moduletitles = ["download\nmodules","time module", "basic Turtle", "os module", "Gui part 1", "Gui part 2",
                "Gui part 3", "Gui part 4"]

projecttitles = ["Turtle star"]

bonustitles = [""]
################################################################################################################

#these are the colors of each section
#"can be edited if colors don't fit your needs"
#_______________________________________________________________________________________
easycol = "Aqua"
mediumcol = "Lime"
hardcol = "OrangeRed"
modulecol = "Teal"
projectcol = "Gold"
bonuscol = "Silver"
#_______________________________________________________________________________________

#some variable lines "should not be edited"
Diffcolors = [easycol, mediumcol, hardcol, modulecol, projectcol, bonuscol]
difficulties = ["easy", "medium", "hard", "modules", "projects", "Bonus codes"]
ObjList = []
filename = ""

#this selects files from the library
def buildpath(filename, difficulty):
    global pathtofiles
    pathtofiles = ""
    droppedFile = sys.argv[0]
    droppedFile = droppedFile.split("\\")
    del droppedFile[-1]
    for each in droppedFile:
        pathtofiles += each + "\\"
    if difficulty == "easy":
        pathtofiles += "easy\\" + filename
    elif difficulty == "medium":
        pathtofiles += "medium\\" + filename
    elif difficulty == "hard":
        pathtofiles += "hard\\" + filename
    elif difficulty == "modules":
        pathtofiles += "modules\\" + filename
    elif difficulty == "projects":
        pathtofiles += "projects\\" + filename
    elif difficulty == "Bonus codes":
        pathtofiles += "Bonus\\" + filename
    openpython(pathtofiles)

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
        
def destroyLabel(Objects):
    global ObjList
    for Obj in Objects:
        Obj.destroy()
    ObjList = []
        
########################################Easy#####################################################
#there are all the settups for each page    
def easySetup():
    global ObjList
    global window

    window.configure(bg=easycol)
    titles = easytitles
    
    easytext = Label(window, text="Basic simple knowledge", height = 5, width=65, bg=easycol)
    easytext.grid(row=1, column=0, columnspan=4)
    ObjList.append(easytext)
    for easystages in range(len(titles)):
        easy = Button(window, text=titles[easystages], bg=easycol,
                      command=lambda number = number, easystages = easystages:number(easystages, "easy"),
                      height = 5, width = 15)
        easy.grid(row = (int(easystages//4)) + 2, column = easystages - (easystages//4)*4)
        ObjList.append(easy)
    
########################################Medium#####################################################
        
def mediumSetup():
    window.configure(bg=mediumcol)
    titles = mediumtitles

    mediumtext = Label(window, text="Basic Highter knowledge", height = 5, width=65, bg=mediumcol)
    mediumtext.grid(row=1, column=0, columnspan=4)
    ObjList.append(mediumtext)
    for mediumstages in range(len(titles)):
        medium = Button(window, text=titles[mediumstages], bg=mediumcol,
                      command=lambda number = number, mediumstages = mediumstages:number(mediumstages, "medium"),
                      height = 5, width = 15)
        medium.grid(row = (int(mediumstages//4)) + 2, column = mediumstages - (mediumstages//4)*4)
        ObjList.append(medium)

########################################Hard#####################################################
        
def hardSetup():
    window.configure(bg=hardcol)
    titles = hardtitles

    hardtext = Label(window, text="Advanced knowledge", height = 5, width=65, bg=hardcol)
    hardtext.grid(row=1, column=0, columnspan=4)
    ObjList.append(hardtext)
    for hardstages in range(len(titles)):
        hard = Button(window, text=titles[hardstages], bg=hardcol,
                      command=lambda number = number, hardstages = hardstages:number(hardstages, "hard"),
                      height = 5, width = 15)
        hard.grid(row = (int(hardstages//4)) + 2, column = hardstages - (hardstages//4)*4)
        ObjList.append(hard)

########################################modules#####################################################
        
def moduleSetup():
    window.configure(bg=modulecol)
    titles = moduletitles

    moduletext = Label(window, text="Modules", height = 5, width=65, bg=modulecol)
    moduletext.grid(row=1, column=0, columnspan=4)
    ObjList.append(moduletext)
    for modulestages in range(len(titles)):
        module = Button(window, text=titles[modulestages], bg=modulecol,
                      command=lambda number = number, modulestages = modulestages:number(modulestages, "modules"),
                      height = 5, width = 15)
        module.grid(row = (int(modulestages//4)) + 2, column = modulestages - (modulestages//4)*4)
        ObjList.append(module)
        
########################################projects#####################################################
        
def projectSetup():
    window.configure(bg=projectcol)
    titles = projecttitles

    projecttext = Label(window, text="Projects", height = 5, width=65, bg=projectcol)
    projecttext.grid(row=1, column=0, columnspan=4)
    ObjList.append(projecttext)
    for projectstages in range(len(titles)):
        project = Button(window, text=titles[projectstages], bg=projectcol,
                      command=lambda number = number, projectstages = projectstages:number(projectstages, "projects"),
                      height = 5, width = 15)
        project.grid(row = (int(projectstages//4)) + 2, column = projectstages - (projectstages//4)*4)
        ObjList.append(project)
        
########################################Bonus codes#####################################################
        
def bonusSetup():
    window.configure(bg=bonuscol)
    titles = bonustitles

    bonustext = Label(window, text="Bonuses and shortcuts", height = 5, width=65, bg=bonuscol)
    bonustext.grid(row=1, column=0, columnspan=4)
    ObjList.append(bonustext)
    for bonusstages in range(len(titles)):
        bonus = Button(window, text=titles[bonusstages], bg=bonuscol,
                      command=lambda number = number, bonusstages = bonusstages:number(bonusstages, "bonus"),
                      height = 5, width = 15)
        bonus.grid(row = (int(bonusstages//4)) + 2, column = bonusstages - (bonusstages//4)*4)
        ObjList.append(bonus)
#__________________________________Pages___________________________________________________________________
###########################################################################################################

def switch(Name):
    global ObjList
    global DifficultyUp
    global DifficultyDown
    destroyLabel(ObjList)

    Number = difficulties.index(Name)
    oneUp = Number + 1
    oneDown = Number - 1
    if oneUp == 6:
        oneUp = 0
    if oneDown == -1:
        oneDown = 5
        
    DifficultyUp.configure(text=difficulties[oneUp],bg = Diffcolors[oneUp],
                           command=lambda difficulties = difficulties:switch(difficulties[oneUp]))
    DifficultyDown.configure(text=difficulties[oneDown], bg = Diffcolors[oneDown],
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
                          bg = Diffcolors[1])
    DifficultyUp.grid(row = 0, column = 3)
    DifficultyDown = Button(window, text=difficulties[5],
                            command=lambda difficulties = difficulties:switch(difficulties[4]), width = 15, height = 5,
                            bg = Diffcolors[5])
    DifficultyDown.grid(row = 0, column = 0)
#_________________________________button changer___________________________________________________________
###########################################################################################################

def createinterface():
    global window
    window = Tk()
    easySetup()
    difficultyswitch()
    window.title("python library")
    window.geometry("460x600")
    window.mainloop()
            
createinterface()
