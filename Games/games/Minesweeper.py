import random
from tkinter import *


Window = Tk()

def resetGame():
    global overlayRow
    global overlayColumn
    global generationContent
    global fieldContainings
    global pureInformationBar
    global lineSize
    global completeFieldOutput
    global cacheNumberForMines
    global buttonColumnPlacement
    global buttonRowPlacement
    global fieldContainings
    overlayRow = 0
    overlayColumn = 0
    generationContent = ["Mine", "Safe", "Safe", "Safe", "Safe", "Safe", "Safe"]
    pureInformationBar = ""
    lineSize = 1
    completeFieldOutput = []
    cacheNumberForMines = 0
    buttonColumnPlacement = 0
    buttonRowPlacement = 0
    fieldSizeGeneration = 0
    fieldContainings = []
    for fieldSizeGeneration in range(Lenght*Lenght):
        fieldContainings.append(random.choice(generationContent))
    spawnButtons()
    edgesDetection()
#test


def spawnButtons():
    global totalFieldGeneration
    global buttonRowPlacement
    global buttonColumnPlacement
    global Lenght
    for totalFieldGeneration in range(Lenght*Lenght):
        Button(Window, command=lambda totalFieldGeneration=totalFieldGeneration: Reveal(totalFieldGeneration), height = 2, width = 8).grid(row=buttonRowPlacement, column=buttonColumnPlacement)
        buttonRowPlacement += 1
        if buttonRowPlacement == Lenght:
            buttonRowPlacement = 0
            buttonColumnPlacement += 1

def edgesDetection():
    global lineSize
    global pureInformationBar
    global Lenght
    global gameFieldSize
    for gameFieldSize in range(Lenght*Lenght):
        pureInformationBar = ""
        #Top
        if gameFieldSize < Lenght:
            pureInformationBar = pureInformationBar + "W"
        else:
            pureInformationBar = pureInformationBar + "A"

        #Left
        if lineSize == 1:
            pureInformationBar = pureInformationBar + "W"
        else:
            pureInformationBar = pureInformationBar + "A"

        #Right
        if lineSize == Lenght:
            lineSize = 0
            pureInformationBar = pureInformationBar + "W"
        else:
            pureInformationBar = pureInformationBar + "A"

        #Bottom
        if gameFieldSize >= (Lenght * Lenght) - Lenght :
            pureInformationBar = pureInformationBar + "W"
        else:
            pureInformationBar = pureInformationBar + "A"
        actualCaseCheck()
        lineSize += 1
#W = Wall
#A = Air

def Mine():
    global cacheNumberForMines
    cacheNumberForMines = "M"
def topLeft():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize - (Lenght + 1)] == "Mine":
        cacheNumberForMines += 1
def topMid():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize - Lenght] == "Mine":
        cacheNumberForMines += 1
def topRight():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize - (Lenght - 1)] == "Mine":
        cacheNumberForMines += 1
def midLeft():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize - 1] == "Mine":
        cacheNumberForMines += 1
def midRight():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize + 1] == "Mine":
        cacheNumberForMines += 1
def bottomLeft():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize + (Lenght - 1)] == "Mine":
        cacheNumberForMines += 1
def bottomMid():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize + Lenght] == "Mine":
        cacheNumberForMines += 1
def bottomRight():
    global cacheNumberForMines
    global fieldContainings
    if fieldContainings[gameFieldSize + (Lenght + 1)] == "Mine":
        cacheNumberForMines += 1

def actualCaseCheck():
    global pureInformationBar
    global fieldContainings
    global gameFieldSize
    global cacheNumberForMines
    if fieldContainings[gameFieldSize] == "Mine":
        Mine()
    elif pureInformationBar == "WWAA":
        midRight()
        bottomMid()
        bottomRight()
    elif pureInformationBar == "WAWA":
        midLeft()
        bottomMid()
        bottomLeft()
    elif pureInformationBar == "AWAW":
        midRight()
        topMid()
        topRight()
    elif pureInformationBar == "AAWW":
        midLeft()
        topMid()
        topLeft()
    else:
        if pureInformationBar[0] == "W":
            midLeft()
            midRight()
            bottomLeft()
            bottomMid()
            bottomRight()
        elif pureInformationBar[1] == "W":
            topMid()
            topRight()
            midRight()
            bottomMid()
            bottomRight()
        elif pureInformationBar[2] == "W":
            topMid()
            topLeft()
            midLeft()
            bottomMid()
            bottomLeft()
        elif pureInformationBar[3] == "W":
            topLeft()
            topMid()
            topRight()
            midLeft()
            midRight()
        else:
            topLeft()
            topMid()
            topRight()
            midLeft()
            midRight()
            bottomLeft()
            bottomMid()
            bottomRight()      
    completeFieldOutput.append(str(cacheNumberForMines))
    cacheNumberForMines = 0

def Reveal(x):
    global overlayRow
    global overlayColumn
    global lenght
    global oneswitch
    if completeFieldOutput[x] == "0":
        colorOfButton = "green"
    elif completeFieldOutput[x] == "M":
        colorOfButton = "red"
        Root = Tk()
        Label(Root, text="You lost").pack()
        Button(Root, text="Reset", command=resetGame).pack()
    elif completeFieldOutput[x] == "1":
        colorOfButton = "DarkOliveGreen1"
    elif completeFieldOutput[x] == "2":
        colorOfButton = "DarkOliveGreen4"
    elif completeFieldOutput[x] == "3":
        colorOfButton = "LightGoldenrod3"
    elif completeFieldOutput[x] == "4":
        colorOfButton = "gold2"
    elif completeFieldOutput[x] == "5":
        colorOfButton = "goldenrod1"
    elif completeFieldOutput[x] == "6":
        colorOfButton = "chocolate2"    
    elif completeFieldOutput[x] == "7":
        colorOfButton = "salmon4"
    elif completeFieldOutput[x] == "8":
        colorOfButton = "firebrick"

    overlayColumn = x//Lenght
    overlayRow = x - (overlayColumn*Lenght)
    Button(Window, text=str(completeFieldOutput[x]), height = 2, width = 8, bg=colorOfButton).grid(row = overlayRow, column = overlayColumn)
    overlayRow = 0
    overlayColumn = 0
    
colorOfButton = ""
Lenght = int(input("Size of field: "))
resetGame()

oneswitch = 0
Window.title("Minesweeper")
Window.geometry("1000x1000")

        

    

