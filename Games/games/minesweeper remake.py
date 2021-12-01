from tkinter import *
import random

#easy = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], "easy")
easy = ([0, 0, 0, 0, 0, 0, 9], "easy")
normal = ([0, 0, 0, 0, 9], "normal")
hard = ([0, 0, 0, 9], "hard")

difficulty = easy
size = 12

#solid variables
def setall():
    global first
    global second
    global numb
    global madeField
    global savedPositions
    global safeStart
    global switch
    global Flagged
    global minePositions
    global flagPositions
    global allOpenned


    first = [-1, 0, 1, -1, 1, -1, 0, 1]
    second = [-1, -1, -1, 0, 0, 1, 1, 1]

    #semi switchable

    numb = 0
    madeField = []
    minePositions = []
    flagPositions = []
    allOpenned = []

    #constantly changing variables
    savedPositions = []
    safeStart = True
    switch = True
    Flagged = ""

def FieldGeneration():
    #creates lists
    global size
    global difficuly
    global first
    global second
    global numb
    global easy
    global normal
    global hard
    global minePositions
    minePositions = []
    fieldsize = size + 2
    if numb == 0:
        difficulty = easy
    elif numb == 1:
        difficulty = normal
    else:
        difficulty = hard
    mineField = []
    appendContent = []
    singleField = 0
    for fieldx in range(fieldsize + 1):
        mineField.append(appendContent)
        appendContent = []
        for fieldy in range(fieldsize):
            #choosing random mine
            singleField = random.choice(difficulty[0])
            #stops the selection to go outside
            if fieldx < 1 or fieldx > size - 2 or fieldy < 1 or fieldy > size - 2:
                singleField = 0
            appendContent.append(singleField)
            if singleField == 9:
                minePositions.append([fieldx, fieldy])
    del mineField[0]
    for scanrow in range(fieldsize - 2):
        for scancolumn in range(fieldsize - 2):
            if mineField[scanrow + 1][scancolumn + 1] > 7:
                for each in range(8):
                    mineField[scanrow + first[each] + 1][scancolumn + second[each] + 1] += 1
    for minex in range(fieldsize - 2):
        for miney in range(fieldsize - 2):
            if mineField[minex + 1][miney + 1] >= 9:
                mineField[minex + 1][miney + 1] = "M"
    Button(window, text="Reset", command=resetField).grid(row = size + 4, column = (size//2)-5,columnspan = 10)
    return(mineField)


def Scanfield(coords):
    global savedPositions
    global safeStart
    global madeField
    global switch
    global first
    global second
    if safeStart == True:
        while madeField[coords[0]][coords[1]] != 0:
            madeField = FieldGeneration()
        safeStart = False  

    #allows to open single cells
    #also reveals all the 0 containing cells
    reveal([coords[0], coords[1]])
    #__________________________________________________
    #start of the group covering code
    if madeField[coords[0]][coords[1]] == 0:
        #checks all fields around another ***
        for each in range(8):
            place1 = coords[0]+first[each]
            place2 = coords[1]+second[each]
            #In the grid
            if(place1 > 0 and place1 < size - 1 and place2 > 0 and place2 < size - 1):
            #Makes that only one specific position can get saved
                if [place1, place2] not in savedPositions:
            #saves position
                    savedPositions.append([place1, place2])
            #reveals and opens all the cells
        reveal([coords[0], coords[1]])
    
    #_______________________________________________________
    #switch stops massive recursions and allows for controlled executions
    if switch == True:
        switch = False
        for element in savedPositions:
            if madeField[element[0]][element[1]] != 0:
                #reveals all walls (numbers around the 0)
                reveal([element[0], element[1]])
            else:
                #if 0 keep scanning
                Scanfield([element[0], element[1]])
        savedPositions = []
        switch = True
    madeField[coords[0]][coords[1]] = "F"

def resetField():
    global window
    window.destroy()
    window = Tk()
    setall()
    settings()
    window.title("Minesweeper")
    window.mainloop()
    

def end(stateOfGame):
    global size
    Label(window, width=4).grid(row = size + 2, column = (size//2)-5, columnspan = 10)
    Label(window, text="you " + stateOfGame).grid(row = size + 3, column = (size//2)-5, columnspan = 10)

def win():
    global switch
    switch = False
    revealall()
    switch = True
    end("won")
    
def reveal(placement):
    global switch
    global minePositions
    global allOpenned
    background = "green"
    if madeField[placement[0]][placement[1]] != "F":
        if madeField[placement[0]][placement[1]] == "M":
            background = "red"
            if switch == True:
                switch = False
                revealall()
                end("lost")
                switch = True
        elif madeField[placement[0]][placement[1]] == 0:
            background = "green"
        elif madeField[placement[0]][placement[1]] == 1:
            background = "seagreen"
        elif madeField[placement[0]][placement[1]] == 2:
            background = "limegreen"
        elif madeField[placement[0]][placement[1]] == 3:
            background = "yellowgreen"
        elif madeField[placement[0]][placement[1]] == 4:
            background = "greenyellow"
        elif madeField[placement[0]][placement[1]] == 5:
            background = "goldenrod"
        elif madeField[placement[0]][placement[1]] == 6:
            background = "darkgoldenrod"
        elif madeField[placement[0]][placement[1]] == 7:
            background = "saddlebrown"
        elif madeField[placement[0]][placement[1]] == 8:
            background = "darkred"
        showing = Button(state = DISABLED, text=madeField[placement[0]][placement[1]], bg = background,
                         width = 3, height = 1)
        showing.grid(row = placement[0], column = placement[1])
        if placement not in allOpenned:
            allOpenned.append(placement)
            if len(allOpenned) == ((size - 2)*(size - 2) - len(minePositions)):
                win()
    
#_____________________________________________________
#win or loose
def revealall():
    global size
    for i in range(size - 2):
        for o in range(size - 2):
            reveal([i + 1, o + 1])
#_____________________________________________________

def generateTerrain():
    global size
    global diffLower
    global difficultyLabel
    global diffHighter
    global sizeLower
    global sizeLabel
    global sizeHighter
    global empty
    global start
    global madeField
    diffLower.destroy()
    difficultyLabel.destroy()
    diffHighter.destroy()
    sizeLower.destroy()
    sizeLabel.destroy()
    sizeHighter.destroy()
    empty.destroy()
    start.destroy()
    madeField = FieldGeneration()
    for rowPlacement in range(size):
        for columnPlacement in range(size):
            #generates buttons of mineField
            clickMe = Button(window,
                             command = lambda rowPlacement = rowPlacement,
                             columnPlacement = columnPlacement :Scanfield([rowPlacement, columnPlacement]),
                             width = 3, height = 1)
            empty = rowPlacement
            clickMe.bind("<Button-3>", lambda empty = empty,
                         rowPlacement = rowPlacement,
                         columnPlacement = columnPlacement :right_click([columnPlacement, rowPlacement], empty))
            clickMe.grid(row = rowPlacement, column = columnPlacement)
            if rowPlacement == 0 or rowPlacement == size - 1 or columnPlacement == 0 or columnPlacement == size - 1:
                clickMe.destroy()

def right_click(place, event):
    global flagPositions
    global minePositions
    Flagged = Button(window, text = "🚩", width = 3, height = 1, bg="royalblue")
    Flagged.grid(row = place[1], column = place[0])
    Flagged.bind("<Button-3>", lambda event = event, Flagged = Flagged, place = place: flagRemove(Flagged, place, event))
    flagPositions.append([place[1], place[0]])
    flagPositions.sort()
    if minePositions == flagPositions:
        win()

def flagRemove(obj, coords, event):
    global flagPositions
    obj.destroy()
    try:
        flagPositions.remove([coords[1], coords[0]])
    except:
        pass
    if minePositions == flagPositions:
        win()

def change(specifications):
    global size
    global difficulty
    global numb
    diff = ["Easy", "Normal", "Hard"]
    if specifications[1] == "D":
        if specifications[0] == "L":
            numb -= 1
            if numb == -1:
                numb += 3
        elif specifications[0] == "H":
            numb += 1
            if numb == 3:
                numb -= 3
        difficultyLabel.configure(text=diff[numb])
    else:
        if specifications[0] == "L":
            size -= 1
            if size == 11:
                size = 42
        elif specifications[0] == "H":
            size += 1
            if size == 43:
                size = 12
        sizeLabel.configure(text=size - 2)
        
        

def settings():
    global size
    global difficulty
    global diffLower
    global difficultyLabel
    global diffHighter
    global sizeLower
    global sizeLabel
    global sizeHighter
    global empty
    global start
    numb = 0

    diffLower = Button(window, text="<", command = lambda change = change :change("LD"))
    diffLower.grid(row = 2, column = 1)

    difficultyLabel = Label(window, text=difficulty[1])
    difficultyLabel.grid(row = 2, column = 2)

    diffHighter = Button(window, text=">", command = lambda change = change :change("HD"))
    diffHighter.grid(row = 2, column = 3)

    sizeLower = Button(window, text="<", command = lambda change = change :change("LF"))
    sizeLower.grid(row = 3, column = 1)

    sizeLabel = Label(window, text=size - 2)
    sizeLabel.grid(row = 3, column = 2)

    sizeHighter = Button(window, text=">", command = lambda change = change :change("HF"))
    sizeHighter.grid(row = 3, column = 3)

    empty = Label(window)
    empty.grid(row = 4)

    start = Button(window, text="Start Game", command = generateTerrain)
    start.grid(row = 5, column = 2)


window = Tk()

setall()

settings()

window.title("Minesweeper")

window.mainloop()




                
