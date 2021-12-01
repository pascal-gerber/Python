from tkinter import *
import random

totalScore = 0

def resetGame():
    global carDoor
    global playerInput
    global ranChoice
    Button(window, text="Door1", command=lambda:click1(), width=25, height=4).grid(row=1, column=1)
    Button(window, text="Door2", command=lambda:click2(), width=25, height=4).grid(row=1, column=2)
    Button(window, text="Door3", command=lambda:click3(), width=25, height=4).grid(row=1, column=3)
    carDoor = random.randint(1, 3)
    playerInput = 0
    ranChoice = "False"
    Label(window, text="Choose a door\n1 door contains a car\nthe 2 others goats.", width=25, height=4).grid(row=5, column=2)

def gameResult():
    global playerInput
    global carDoor
    global totalScore
    if carDoor == playerInput:
        totalScore += 1
        Label(window, text="wins: " + str(totalScore)).grid(row=7, column=2)    
        Label(window, text="You Won Congrats", width=25, height=4).grid(row=5, column=2)
        Button(window, text="reset", bg="green", command=resetGame).grid(row=4, column=2)
        for lock in range(4):
            if lock == 0:
                continue
            Button(window, text="you won", bg="green", width=25, height=4).grid(row=1, column=lock)
    
    else:
        Label(window, text="You Lost", width=25, height=4).grid(row=5, column=2)
        Button(window, text="reset", bg="green", command=resetGame).grid(row=4, column=2)
        totalScore -= 1
        Label(window, text="wins: " + str(totalScore)).grid(row=7, column=2)
        for lock in range(4):
            if lock == 0:
                continue
            Button(window, text="you lost", bg="red", width=25, height=4).grid(row=1, column=lock)
    

def swapDoor():
    global playerInput
    global swapPlace
    playerInput = swapPlace
    gameResult()

def lockWromg():
    global wromgDoor
    global swapPlace
    global playerInput
    global i
    if wromgDoor == 1:
        i = 1
    elif wromgDoor == 2:
        i = 2
    else:
        i = 3
    swapPlace = (6-(i+playerInput))
    Button(window, text="There was a goat", bg="red", width=25, height=4).grid(row=1, column=i)
    Button(window, text="You choose this\nclick to stay", bg="green", command=gameResult, width=25, height=4).grid(row=1, column=playerInput)
    Button(window, text="Swap place here", bg="yellow", command=swapDoor, width=25, height=4).grid(row=1, column=swapPlace)
    Label(window, text="Do you want to swap or stay?").grid(row=2, column=2)
        

def check():
    global carDoor
    global ranChoice
    global playerInput
    if carDoor == playerInput:
        ranChoice = "True"
        
def click1():
    global playerInput
    global ranChoice
    global wromgDoor
    choiceNumbs = ("2", "3")
    playerInput = 1
    check()
    if ranChoice == "True":
        wromgDoor = int(random.choice(choiceNumbs))
    else:
        if playerInput == 2:
            wromgDoor = 3
        else:
            wromgDoor = 2
    lockWromg()
    
    
def click2():
    global playerInput
    global ranChoice
    global wromgDoor
    choiceNumbs = ("1", "3")
    playerInput = 2
    check()
    if ranChoice == "True":
        wromgDoor = int(random.choice(choiceNumbs))
    else:
        if playerInput == 1:
            wromgDoor = 3
        else:
            wromgDoor = 1
    lockWromg()
    
def click3():
    global playerInput
    global ranChoice
    global wromgDoor
    choiceNumbs = ("1", "2")
    playerInput = 3
    check()
    if ranChoice == "True":
        wromgDoor = int(random.choice(choiceNumbs))
    else:
        if playerInput == 1:
            wromgDoor = 2
        else:
            wromgDoor = 1
    lockWromg()

window = Tk()
resetGame()
window.geometry("700x500")
window.title("goat game")
window.mainloop()
