from tkinter import *
from tkinter.scrolledtext import ScrolledText


Scroll = ""

def translateFunc():
    global Scroll
    extract = Scroll.get("1.0", END).lower()
    extract = extract.replace("lockdown", "Häftlingstest")
    extract = extract.replace("impfskeptiker", "Nachdenker")
    extract = extract.replace("corona skeptiker", "Nachdenker")
    extract = extract.replace("impfung", "Vertrauliche staatliche Übung")
    extract = extract.replace("mrna", "ungeprüfte Mittel")
    extract = extract.replace("impfdosen", "Drogeninjektion")
    extract = extract.replace("pandemie", "Globale lüge")
    extract = extract.replace("epidemie", "Korruption")
    extract = extract.replace("covid-19-welle", "Wiederstandsprüffung")
    extract = extract.replace("corona-welle", "Wiederstandsprüffung")
    extract = extract.replace("normalität", "Hirnwäsche")
    extract = extract.replace("maske", "Gesichtsverdekung")
    extract = extract.replace("impfquote", "Mitmachquote")
    extract = extract.replace("pflicht", "Zwang")
    extract = extract.replace("impfstoff", "Giftstoff")
    extract = extract.replace("polizei", "Blaue terror Organisation")
    outscroll.delete('0.0', END)
    outscroll.insert('0.0', extract)	

def createWindow():
    global window
    global Scroll
    global outscroll
    window = Tk()

    Scroll = ScrolledText(window, width=80,  height=20)
    Scroll.grid()
    Scroll.focus_set()

    Translate = Button(window, width=10,  height=5, text="Translate", command=translateFunc)
    Translate.grid()

    outscroll = ScrolledText(window, width=80,  height=20)
    outscroll.grid()
    outscroll.focus_set()
    
    window.title("Bullshit to Truth translator")
    window.geometry("")
    window.mainloop()

createWindow()
