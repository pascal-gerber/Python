from tkinter import *
import string
import pyperclip

a = ('ꖌ', 'ᒷ', '⋮', 'ᒲ', '⨅', 'ʖ', 'ℸ', 'ᑑ', '/', '⍑', 'ᔑ', '∷', '∴', '|', 'ꖎ', '¡', 'リ', '⚍', '!', '⎓', '╎', '⊣', 'ᓭ', '↸', 'ᓵ', '⍊')
letters = string.ascii_lowercase

def encode():
    global a
    global letters
    global user
    global newstring
    global contained
    global Usertext
    global Output
    user = Usertext.get()
    newstring = ""
    for Letter in user.lower():
        contained = False
        for new in range(len(a)):
            if letters[new] == Letter:
                newstring += a[new]
                contained = True
        if contained == False:
            newstring += Letter
    Output.configure(text=str(newstring))
    pyperclip.copy(newstring)

def decode():
    global a
    global letters
    global user
    global newstring
    global contained
    global Usertext
    global Output
    user = Usertext.get()
    newstring = ""
    for Letter in user.lower():
        contained = False
        for new in range(len(a)):
            if a[new] == Letter:
                newstring += letters[new]
                contained = True
        if contained == False:
            newstring += Letter
    Output.configure(text=str(newstring))
    pyperclip.copy(newstring)

def createNewWindow():
    global Usertext
    global Output
    window = Tk()
    Label(window, text="Minecraft language").grid(row = 1, column = 1)
    Usertext = Entry(window)
    Usertext.grid(row = 2, column = 1)
    Usertext.focus_set()
    Encode = Button(window, text="Encode text", command=encode).grid(row = 3, column = 1)
    Decode = Button(window, text="Decode text", command=decode).grid(row = 3, column = 2)
    Output = Label(window)
    Output.grid(row = 4, column = 1)
    window.geometry("500x500")
    window.title("Minecraft text")
    window.mainloop()

createNewWindow()






















