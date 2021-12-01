from tkinter import *
import time

# time.ctime(time.time()))
# is for nowerday

def reset():
    global clicks
    global startTime
    startTime = 0
    clicks = 0
    

def start():
    global startTime
    global spamButton
    startTime = int(time.time())
    spamButton.configure(command = clickMe, text = "Spam")

def empty():
    pass

def clickMe():
    global clicks
    global startTime
    clicks += 1
    if startTime + 10 <= int(time.time()):
        Label(window, text="Clicks : " + str(clicks)).grid()
        spamButton.configure(command = empty)
        Label(window, text="Clicks per sec : " + str(clicks/10) + "/S").grid()

window = Tk()


reset()
spamButton = Button(window, text="Spam me", command=start, width=10, height=5)
spamButton.grid()


window.geometry("500x500")
window.mainloop()
