from tkinter import *
import time
import threading

def startValues():
    global Coins
    global clickWorth
    global coinPerSecond
    global rivellaAmount
    global beefAmount
    global reset
    Coins = 0
    coinPerSecond = 0
    rivellaAmount = 1
    beefAmount = 1

clickWorth = 1

standpoint = 1

rivMult = 2.5
beefMult = 5.6

reset = ""

def buyAutoClicker(amount, obj):
    global coinPerSecond
    global rivellaAmount
    global beefAmount
    global Coins
    global Rivella
    global rivMult
    global beefMult
    if obj == "rivella":
        cost = rivellaAmount*rivMult
        if Coins >= cost: 
            coinPerSecond += amount*rivMult
            Coins -= cost
            rivellaAmount += 1
            Rivella.configure(text="Buy Rivella (+" + str(rivMult) + " CPS) " + str(round(rivellaAmount*rivMult, 2)) + "cost")    
    elif obj == "beef":
        cost = beefAmount*beefMult
        if Coins >= cost: 
            coinPerSecond += amount*beefMult
            Coins -= cost
            beefAmount += 1
            BEEF.configure(text="Buy Beef jerky (+" + str(beefMult) + " CPS) " + str(round(beefAmount*beefMult, 2)) + "cost")
    

def autoClick():
    global Coins
    global coinPerSecond
    while 1:
        Coins += coinPerSecond
        updateLabel()
        checkreset()
        time.sleep(1)

def updateLabel():
    global Coins
    global showCoins
    showCoins.configure(text=str(round(Coins, 2)) + " coins")

def click():
    global Coins
    global clickWorth
    Coins += clickWorth
    updateLabel()

def checkreset():
    global Coins
    global standpoint
    global reset
    if Coins >= standpoint * 1000:
        reset = Button(window, text="MultiplierUpgrade", command = resetgame)
        reset.grid(row=10, column=1)

def resetgame():
    global reset
    reset.destroy()
    global Coins
    global standpoint
    global rivMult
    global beefMult
    global clickWorth
    if Coins >= standpoint * 1000:
        rivMult = round(rivMult*1.5, 2)
        beefMult = round(beefMult*1.5, 2)
        clickWorth = clickWorth*2
        standpoint = standpoint*2
        startValues()
        createInterface()
        
        
def createInterface():
    global showCoins
    global Clicker
    global Rivella
    global BEEF
    global rivMult
    showCoins = Label(window, text=str(Coins) + " coins", width = 20, height = 3)
    showCoins.grid(row = 1, column = 1)
    Clicker = Button(window, text="click to get " + str(clickWorth) + " Coins", command=click, width = 20, height = 5)
    Clicker.grid(row = 2, column = 1)
    
    Rivella = Button(window, text="Buy Rivella (+" + str(rivMult) + " CPS) " + str(rivellaAmount*rivMult) + "cost", command=lambda buyAutoClicker = buyAutoClicker: buyAutoClicker(1, "rivella"), width = 40, height = 5)
    Rivella.grid(row = 3, column = 1)

    BEEF = Button(window, text="Buy Beef jerky (+" + str(beefMult) + " CPS) " + str(beefAmount*beefMult) + "cost", command=lambda buyAutoClicker = buyAutoClicker: buyAutoClicker(2, "beef"), width = 40, height = 5)
    BEEF.grid(row = 4, column = 1)

window = Tk()

startValues()
createInterface()

addautoclick = threading.Thread(target=autoClick)
addautoclick.start()

window.title("Clicker")
window.geometry("500x500")
window.mainloop()
