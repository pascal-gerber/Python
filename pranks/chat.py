from tkinter import *
import time
import random
import threading
import re
import os


newNumb = 100
objectList = []
output = ""

spamm = ""
spamList = 0

maxi = 10
mini = 3

noMultimessages = True

werbistdu = 0

def AnswerToperson(text):
    global newNumb
    global objectList
    global output
    global spamm
    global spamList
    global maxi
    global mini
    global noMultimessages
    global Chat
    global werbistdu
    if noMultimessages == True:
        noMultimessages = False
        time.sleep(random.randint(mini, maxi))
        elsewords = ["oof", "wie meinsch?", "was meinsch du?", "was?", "u du was machsch?", "längwillig?"]
        mathanswers = [" heh bi guet i dem", " easy", " im kopf grechnet"]
        text = text.lower()
        output = ""
        newtext = ""
        try:
            newtext = re.findall("([0-9]+[+-\/*][0-9]+)", text)
            output = (str(eval(newtext[0])) + random.choice(mathanswers))
        except:
            if "hey" in text or "hello" in text or "hallo" in text or "yo" in text or "hi" in text:
                output = random.choice(["hey ", "hallo ", "Heyy ", "ey "])
                if "päscu" in text:
                    output += random.choice(["Roman? ", "Philip? ", "Nick? "])
            if "pascal" in text and len(text) < 10:
                output = random.choice(["jep de bi ig", "jep"])
            if "guet" in text:
                output += random.choice(["okay nice", "was machsch so?"])
            if "chat" in text:
                output += random.choice(["danke selbscht gmacht", "gäü isch cool", "danke :D"])
            if "wie gehts" in text or "geits" in text:
                output += random.choice(["geit so u dir? ", "Naja chli streng, u du? ", "Cha besser ga.. ", "Mues, Mues... "])
            if "geit guet" in text or "geht gut" in text:
                output += random.choice(["okay cool ", "Nice ", ":D", "Very good"])
            if "was isch" in text or "passiert?" in text:
                output += random.choice(["niid viel", "mir isch längwillig", "niid so viel wirklich"])
            if "was machsch" in text or "was machst du" in text:
                output += random.choice(["Chli programmiere ", "chli code schriibe ", "chli python schriibe ", "es cool programm mache"]) 
            if "(:" in text or ":D" in text or ":)" in text or ":b" in text:
                output += random.choice(["(:", ":b", ":D", ":]"])
            if "krass " in text or text == "ok":
                output += random.choice(["und was machsch du? ", ":b", "jep"])
                maxi = 10
                mini = 3
            if "schlecht" in text or "traurig" in text or "truurig" in text or "schlächt" in text:
                output = random.choice(["was isch den passiert?", "?", "wieso?"])
                maxi = 3
                mini = 1
            if "arbeit ha" in text or "arbeite" in text or "schaffe" in text:
                output = random.choice(["oh okay", "störe di nümm", "okay", "ohh..."])
            if "wow" in text:
                output += random.choice(["gaü geil?", "jep wow", "sehr cool"])
                maxi = 10
                mini = 3
            if "echt?" in text or "wie?" in text or "ächt?" in text:
                output = random.choice(["natürlich", "total echt", "immer doch"])
            if "ernsthaft" in text or "wirkli" in text:
                output = random.choice(["ja wirklich!", "ernsthaft", "kei scheiss"])
            if "siech" in text:
                output = random.choice(["get pranked", "heh", "voll drii gheit"])
            if "nein" in text or "nei" in text:
                output = random.choice(["wieso nei?", "nei?", "okay..."])
            if "bist du" in text or "heisst du" in text or "dein name" in text or "bisch" in text or "heissisch" in text or "di name" in text:
                output = random.choice(["pascal", "i biis der pascal", "i biis, der pascal", "pascal :D"])
                werbistdu += 1
                if werbistdu == 3 or werbistdu == 4:
                    output = random.choice(["wer bini schüsch?", "wer sött ig schusch sii?", "logisch das igs bii"])
                elif werbistdu == 5 or werbistdu == 6:
                    output = random.choice(["...", "wow", "immer no am frage...", "okay...", "du weisch es eh selber"])
                elif werbistdu > 6:
                    output = ""
            if text == "ja" or text == "jo":
                output = random.choice(["was wetsch de mache?", "was sii dini plän?", "okay"])
            if "spiele" in text:
                output = "chasch"
            if "program" in text or "programmiert" in text:
                output = random.choice(["jep selbst programmiert (:", "selbscht griibe", "ohni hilf selbscht gmacht"])
            if "tschüss" in text or "bye" in text or "bis später" in text or "muess" in text:
                output = random.choice(["tschüss", "bye", "biss nochher oder später"])
            if text == "spamcode":
                spamming = ["Niid spämmä bitte", "Wow spam...", "okay... has verstande"]
                output = random.choice(spamming)
            if text == "bancode":
                output = random.choice(["leider hanni no khe ban chnopf", "bitte spam niid", "oof", "chasch mall öpis anders sege als (" + str(text) + ")"])
            if "ausgang?" in text or "uusgang?" in text:
                output = random.choice(["nei, niid wirkli", "no nie wirkli gange, wieso?", "nei?"])
            if "längwillig?" in text or "langweilig?" in text:
                output = random.choice(["scho eigendli", "naja nüüt besseres ztue", "meehhh"])
            if text == "nice" or text == "a nice":
                output = random.choice(["total", ":D", "i weiss"])
            if "bisch dran" in text or "was schriibsch" in text or "am schriibe" in text or "programmiersch?" in text:
                output = random.choice(["text antworter", "chatbots", "experiments"])
            if "störsch niid" in text or "nid am störe" in text or "störst nicht" in text:
                output = random.choice(["nice", "also guet", "okay guet"])
            if text == "okay" or text == "ok":
                output += random.choice(["ok", "okay", ":D"])
            if "chum" in text or "komm" in text:
                output = "chume "
                if "pause" in text:
                    output += random.choice(["i d'pause", ", bii grad da"])
                elif "here" in text or "härä" in text or "hie" in text or "verbii" in text:
                    output += "mau"
            if "corona" in text or "covid" in text:
                output = random.choice(["sollte dir nicht ein zwang geben", "Sollte nicht zu dein problem werden"])
            if "berset" in text or "parmelin" in text:
                output = random.choice(["beh er ist eh ein komischer typen", "hat mehr macht als die bundesverfassung"])
                if "corona" in text or "covid":
                    output = random.choice(["er nützt covid eh nur aus für sein geld", "hat bundesverfassung damit überfahren"])
    
            if len(output) == 0:
                output = random.choice(elsewords)
        noMultimessages = True
        Chat = Label(window, text="User 1: " + output)
        Chat.grid(row=newNumb, column=1)
        objectList.append(Chat)
        newNumb -= 1
        tryClearchat()


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

