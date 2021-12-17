from tkinter import *
import random

#both variable will be Buttons
doorList = []
currentSelected = None

resetParameters = []

#first part will be executed when the first button is clicked
#it will configure all buttons to the specific state needed
def firstpart(numb):
    nowselected = doorList[numb]
    cardoor = random.choice(doorList)
    #the for loop will make every button apear as changeable so
    #that the last choice will show up as changable
    for i in doorList:
        i.configure(text="do you want to change",
                    command=lambda i = i, cardoor = cardoor:secondpart(cardoor, i),
                    bg="Yellow")
    #now the specific selected button cannot be deleted since
    #it is the selected, so we ask the user if he wants to stay
    nowselected.configure(text="Do you want\nto stay?")
    doorList.remove(nowselected)
    #the list it removes it from is for part 2, so it cannot remove
    #the selected button from the goat reveal door

    #a try is needed since if the door already has been removed
    #it whould not raise any error################
    try:
        doorList.remove(cardoor)
    except:
        pass
    ##############################################

    #now from the eaten list it will choose the last 1 or 2 remaining
    #doors with the goat door
    goatdoor = random.choice(doorList)
    goatdoor['state'] = DISABLED
    goatdoor.configure(text="i am a goat", bg="Grey")
    #it will simply remove the option

#second part will only differenciate betwem the selected second button
#and the car button
def secondpart(cardoor, selected):
    global resetParameters
    #very simply checking if the selected is the same as the car
    if cardoor == selected:
        cardoor.configure(text="you won", bg="Green")
    else:
        selected.configure(text="you lost", bg="Red")
        cardoor.configure(text="this was the car", bg="Yellow")
        #and make you loose or win
    cardoor['state'] = DISABLED
    selected['state'] = DISABLED
    #emptyspace will create a space
    emptyspace = Label(window, height=8).grid(row=2, column=1)
    ResetButton = Button(text="reset game", command=reset, height = 5, width=20)
    ResetButton.grid(row=3, column=1)
    resetParameters.append(ResetButton)

#deletes every object and resets the field
def reset():
    global resetParameters
    for each in resetParameters:
        each.destroy()
    creategame()
        


#the start needs to be a function since it will allow to reset the game
def creategame():
    global doorList
    global resetParameters
    #resets parameters
    doorList = []
    currentSelected = None
    resetParameters = []
    #generates all 3 buttons
    for i in range(3):
        Clickme = Button(window, text="door nr:" + str(i + 1), command=lambda i = i:firstpart(i),
                         height = 10, width=20)
        Clickme.grid(row=1, column=i)
        doorList.append(Clickme)
        resetParameters.append(Clickme)




window = Tk()

Text = Label(window, text="Choose one door, theres a car and 2 goats")
Text.grid(row=0, column=0, columnspan=3)

creategame()


window.geometry("500x500")
window.mainloop()
