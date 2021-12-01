from tkinter import *
import random
import time
import pyperclip
    
#Defines the variables as "existant"
encValueOne = ""
encValueTwo = ""
encValueThree = ""

wholeValue = ""
Codex = ""
save = ""

addBack = ""
divideBack = ""
substractBack = ""
endWorth = ""

#Encodes the section + adds secret key in message
def encSave(x, y):
    global Codex
    global wholeValue
    global save
    for i in (save):
        wholeValue += chr(eval(str(ord(i)) + y + str(x)))
    save = wholeValue   
    if y == "+":
        Codex += chr(int("1" + str(x)))
    elif y == "-":
        Codex += chr(int("2" + str(x)))
    elif y == "*":
        Codex += chr(int("3" + str(x)))
    wholeValue = ""

#will read the user Entries
def add(key):
    encSave(str(key), "+")
    
def substract(key):
    encSave(str(key), "-")
    
def multiply(key):
    encSave(str(key), "*")
    
#-------------------------------------------------
#Button functions
#Encodes text in the written field
def encode():
    global save
    global Codex
    save = encoderField.get()
    add(str(additionField.get()))
    multiply(str(multiplicationField.get()))
    substract(str(substractionField.get()))
    decoderField.delete(0, END)
    decoderField.insert(0, str(save) + str(Codex))
    pyperclip.copy(str(save) + str(Codex))
    Codex = ""
    showUser = Label(Window, text = "your encoded text \nhas been copied\n to the clipboard")
    showUser.grid(row=11, column=4)
    
#Decodes the text on the other
def decode():
    global addBack
    global divideBack
    global substractBack
    global endWorth
    value = decoderField.get()
    addBack = str(ord(value[len(value)-1]))
    divideBack = str(ord(value[len(value)-2]))
    substractBack = str(ord(value[len(value)-3]))
    addBack = addBack[1:len(addBack)]
    divideBack = divideBack[1:len(divideBack)]
    substractBack = substractBack[1:len(substractBack)]
    text = value[0:len(value)-3]
    for letter in text:
        endWorth += (chr(int(((ord(letter) + int(addBack)) / int(divideBack)) - int(substractBack))))
    encoderField.delete(0, END)
    encoderField.insert(0, str(endWorth))    
    endWorth = ""
    
#Randomizes all 3 numbers in the key
def randomize():
    additionField.delete(0, END)
    additionField.insert(END, str(random.randint(10, 99)))
    substractionField.delete(0, END)
    substractionField.insert(END, str(random.randint(10, 99)))
    multiplicationField.delete(0, END)
    multiplicationField.insert(END, str(random.randint(10, 99)))
#-------------------------------------------------
#window section
Window = Tk()

#Information to user
Label(Window, text="preferably get a 2 digit\nNumber on each key.\n(can also be more)").grid(row=11, column=2)

#Buttons
encodeFunction = Button(Window, text="Encode text", command=encode)
encodeFunction.grid(row=4, column=4)

decodeFunction = Button(Window, text="Decode text", command=decode)
decodeFunction.grid(row=4, column=6)

Label(Window).grid(row=9)
randomize = Button(Window, text="Randomize key", command=randomize)
randomize.grid(row=10, column=2)

#this whole section is the layout
#line cutter
Label(Window).grid(row=1, column=1)
Label(Window, text="|").grid(row=2, column=3)
Label(Window, text="|").grid(row=3, column=3)
Label(Window, text="|").grid(row=4, column=3)
Label(Window, text="|").grid(row=2, column=5)
Label(Window, text="|").grid(row=3, column=5)
Label(Window, text="|").grid(row=4, column=5)

#addition Entry
additionField = Entry(Window)
additionField.grid(row=3, column=2)
additionField.focus_set()
Label(Window, text="addition key", width=20).grid(row=2, column=2)

#Substraction Entry
substractionField = Entry(Window)
substractionField.grid(row=5, column=2)
substractionField.focus_set()
Label(Window, text="substraction key").grid(row=4, column=2)

#Multiplication Entry
multiplicationField = Entry(Window)
multiplicationField.grid(row=7, column=2)
multiplicationField.focus_set()
Label(Window, text="multiplication key").grid(row=6, column=2)

#Encoder Field
encoderField = Entry(Window)
encoderField.grid(row=3, column=4)
encoderField.focus_set()
Label(Window, text="Write a text to encode", width=20).grid(row=2, column=4)

#Decoder Field
decoderField = Entry(Window)
decoderField.grid(row=3, column=6)
decoderField.focus_set()
Label(Window, text="Paste a text to decode", width=20).grid(row=2, column=6)

#Window layout and settup
Window.title("Encoder/decoder")
Window.geometry("500x500")
Window.mainloop()

