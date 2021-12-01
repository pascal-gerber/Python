from tkinter import *
import time
import random
import threading
import re
import os


newNumb = 100

objectList = []
output = ""
previous = ""
spamm = ""
spamList = 0

maxi = 10
mini = 3

noMultimessages = True

werbistdu = 0

learn = False

def AnswerToperson(text):
    global newNumb
    global objectList
    global output
    global spamm
    global spamList
    global maxi
    global mini
    global noMultimessages
    global learn
    global previous
    if noMultimessages == True:
        noMultimessages = False
        #time.sleep(random.randint(mini, maxi))

        try:
            inteligence = open("answers.txt", "r")
            info = inteligence.read()
            inteligence.close()
            readOutput = re.findall(("((" + str(text) + "\ )[^\~]*)"), info)
            output = readOutput[0][0].replace(str(text) + " ", "", 1)
        except:
            output = text
            learn = True
            
        if learn == True:
            learn = False
            inteligence = open("answers.txt", "a")
            inteligence.write("\n" + previous + " " + text + "~")
            inteligence.close()
                
        
        noMultimessages = True
        Chat = Label(window, text="User 1: " + output)
        Chat.grid(row=newNumb, column=1)
        objectList.append(Chat)
        newNumb -= 1
        tryClearchat()
        
        previous = text


def tryClearchat():
    global newNumb
    global objectList
    if newNumb == 1:
        newNumb = 100
        for each in objectList:
            each.destroy()
        Chat = Label(window, text="chat cleared")
        Chat.grid(row=newNumb, column=1)
        objectList.append(Chat)
        newNumb -= 1

def sendAndReceive(Input):
    global newNumb
    global objectList
    global noMultimessages
    global spamm
    global spamList
    global text
    global Chat
    Chat = Label(window, text="you: " + Input)
    Chat.grid(row=newNumb, column=1)
    objectList.append(Chat)
    newNumb -= 1
    tryClearchat()
    if spamm == Input:
        spamList += 1
    else:
        spamList = 0
    spamm = Input
    if spamList > 3 and spamList <= 10:
        forchat = threading.Thread(target=AnswerToperson("spamcode"))
        forchat.start()
    elif spamList > 10:
        forchat = threading.Thread(target=AnswerToperson("bancode"))
        forchat.start()
    else:
        forchat = threading.Thread(target=lambda Input = Input:AnswerToperson(Input))
        forchat.start()
    

def createInterface():
    chatEntry = Entry(window)
    chatEntry.grid(row=1, column=1)
    Button(window, text="Send message", command=lambda chatEntry = chatEntry :sendAndReceive(chatEntry.get())).grid(row=1, column=2)    

window = Tk()

createInterface()

window.title("Chat")
window.geometry("500x500")
window.mainloop()

