from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re

Scroll = ""

def translateFunc():
    global Scroll
    extract = Scroll.get("1.0", END).lower()
    extract = extract.replace("verbessern", "verbessere")
    extract = extract.replace("aussieht", "ousgse")
    extract = extract.replace("ausieht", "ousgse")
    extract = extract.replace("brauche", "bruuch")
    extract = extract.replace("sieht", "gseht")
    extract = extract.replace("kann ich", "chani")
    extract = extract.replace("kannst du", "chasch")
    extract = extract.replace("kannst", "chasch")
    extract = extract.replace("schweiz", "schwiiz")
    extract = extract.replace("deutsch", "dütsch")
    extract = extract.replace("willst du", "wetsch")
    extract = extract.replace("willst", "wetsch")
    extract = extract.replace("meinte", "meint")
    extract = extract.replace("einen", "ä")
    extract = extract.replace("sagen", "sägä")
    extract = extract.replace("will ich", "wetti")
    extract = extract.replace("jetzt", "jitz")
    extract = extract.replace("einfach", "eifach")
    extract = extract.replace("hilf", "höuf")
    extract = extract.replace("verbessern", "verbessere")
    extract = extract.replace("geht", "geit")
    extract = extract.replace("schon", "scho")
    extract = extract.replace("gutes", "guets")
    extract = extract.replace("gut", "guet")
    extract = extract.replace("siehst du", "gsesch")
    extract = extract.replace("ich sehe es", "i gsess")
    extract = extract.replace("ich sehe", "i gse")
    extract = extract.replace("sehen", "gse")
    extract = extract.replace("machst du", "machsch")
    extract = extract.replace("marienkäfer", "Hemmugüegli")
    extract = extract.replace("bauch", "ranzä")
    extract = extract.replace("kopf", "grind")
    extract = extract.replace("fuss", "scheichä")
    extract = extract.replace("leute", "lüüt")
    extract = extract.replace("zeit", "ziit")
    extract = extract.replace("gib es", "gibs")
    extract = extract.replace("gibt es", "gits")
    extract = extract.replace("sprechen", "redä")
    extract = extract.replace("sprich", "redt")
    extract = extract.replace("essen", "ässe")
    extract = extract.replace("der", "dr")
    extract = extract.replace("die ", "d'")
    extract = extract.replace("das ", "ds")
    extract = extract.replace("ist ", "isch ")
    extract = extract.replace("nicht", "niid")
    extract = extract.replace("er ", "är ")
    extract = extract.replace("sie", "se")
    extract = extract.replace("nach", "nachä")
    extract = extract.replace("hat", "het")
    extract = extract.replace("habe", "ha")
    extract = extract.replace("ich ", "i ")
    extract = extract.replace("arbeiten", "schaffe")
    extract = extract.replace("müde", "müed")
    extract = extract.replace("viel", "feü")
    extract = extract.replace("euer", "üür")
    extract = extract.replace("kann", "cha")
    extract = extract.replace("dir", "dr")
    extract = extract.replace("k", "ch")
    enEnding = re.findall("([\w]+(en){1})", extract)
    for each in enEnding:
        extract = extract.replace(each[0], each[0][0:-2] + "e")
    outscroll.delete('0.0', END)
    outscroll.insert('0.0', extract)	

def createWindow():
    global window
    global Scroll
    global outscroll
    window = Tk()

    Scroll = ScrolledText(window, width=100,  height=20)
    Scroll.grid()
    Scroll.focus_set()

    Translate = Button(window, width=10,  height=5, text="Translate", command=translateFunc)
    Translate.grid()

    outscroll = ScrolledText(window, width=100,  height=20)
    outscroll.grid()
    outscroll.focus_set()
    
    window.title("German to swissgerman translator")
    window.geometry("")
    window.mainloop()

createWindow()
