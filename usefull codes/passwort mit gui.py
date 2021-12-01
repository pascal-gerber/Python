from tkinter import *
import random
import string
import datetime

def reset():
    global first
    global second
    global thirth
    global types
    first = 0
    second = 0
    thirth = 0
    types = (string.ascii_lowercase)
    
def Generieren():
    global first
    global second
    global thirth
    global wholePassword
    global gnPw
    global types
    if simple == 1:
        reset()
        lenght = int(text.get())
        silabs = ("a", "e", "i", "o", "u", "y")
        consones = ("sh", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "qu", "r", "s", "t", "u", "v", "w", "x", "z", "r", "y")
        gnPw = ""
        for i in range(lenght//2):
            gnPw = gnPw + random.choice(consones) + random.choice(silabs)
    else:
        lenght = int(text.get())
        if first == 1:
            types = types + str(string.ascii_uppercase)
        if second == 1:
            types = types + str(string.digits)
        if thirth == 1:
            types = types + str(string.punctuation)
        for wholePw in range(lenght):
            gnPw = gnPw + types[random.randint(0, len(types) - 1)]
    passwort.delete(0, END)
    passwort.insert(0, gnPw)
    gnPw = ""
    
def speichern():
    writeline = (passwort.get())
    pwtosafe = open(str(Name.get()) + ".txt", "w")
    pwtosafe.write(writeline + "\n\nCreated at :\n" + str(datetime.datetime.now()))
    pwtosafe.close()
#speichern

def uppercase():
    global first
    global types
    if first == 0:
        upper = Button(window, text="Upper", bg="green", width=30, command=uppercase, height=5).grid(row=2, column=1)
        first = 1
    else :
        upper = Button(window, text="Upper", width=30, command=uppercase, height=5).grid(row=2, column=1)
        first = 0
        types = (string.ascii_lowercase)
def Numb():
    global second
    global types
    if second == 0:
        num = Button(window, text="Numbers", bg="green", width=30, command=Numb, height=5).grid(row=2, column=2)
        second = 1
    else :
        num = Button(window, text="Numbers", width=30, command=Numb, height=5).grid(row=2, column=2)
        second = 0
        types = (string.ascii_lowercase)
def Sign():
    global thirth
    global types
    if thirth == 0:
        signs = Button(window, text="Signs", width=30, bg="green", command=Sign, height=5).grid(row=2, column=3)
        thirth = 1
    else:
        signs = Button(window, text="Signs", width=30, command=Sign, height=5).grid(row=2, column=3)
        thirth = 0
        types = (string.ascii_lowercase)
def words():
    global simple
    global types
    if simple == 0:
        Word = Button(window, text="Words", width=30, bg="green", command=words, height=5).grid(row=4, column=1)
        simple = 1
        upper = Button(window, text="Simple mode", bg="red", width=30, height=5).grid(row=2, column=1)
        num = Button(window, text="Simple mode", bg="red", width=30, height=5).grid(row=2, column=2)
        signs = Button(window, text="Simple mode", bg="red", width=30, height=5).grid(row=2, column=3)
    else:
        Word = Button(window, text="Words", width=30, command=words, height=5).grid(row=4, column=1)
        simple = 0
        upper = Button(window, text="Upper", width=30, command=uppercase, height=5).grid(row=2, column=1)
        num = Button(window, text="Numbers", width=30, command=Numb, height=5).grid(row=2, column=2)
        signs = Button(window, text="Signs", width=30, command=Sign, height=5).grid(row=2, column=3)
        types = (string.ascii_lowercase)
        reset()
#diesen langen text ist nur da für die "OK" felder

gnPw = ""
wholePassword = ""
types = (string.ascii_lowercase)
first = 0
second = 0
thirth = 0
simple = 0

window = Tk()

pw = Label(window, text="This is the password", bg="light blue").grid(row=7, column=1)
fn = Label(window, text="Write the name of the file", bg="light blue").grid(row=11, column=1)
space = Button(window, text="Generate password", command=Generieren).grid(row=8, column=2)

text = Entry(window)
text.grid(row=1, column=2)
passwort = Entry(window)
passwort.grid(row=7, column=2)
Name = Entry(window)
Name.grid(row=11, column=2)
#Die 3 Texteingaben

text.focus_set()
Name.focus_set()
passwort.focus_set()
#weiss ich selber nicht aber hilft beim convertieren

upper = Button(window, text="Upper", width=30, command=uppercase, height=5).grid(row=2, column=1)
numb = Button(window, text="Numbers", width=30, command=Numb, height=5).grid(row=2, column=2)
signs = Button(window, text="Signs", width=30, command=Sign, height=5).grid(row=2, column=3)
Word = Button(window, text="Words", width=30, command=words, height=5).grid(row=4, column=1)
#Die 4 Effect Knöpfe auf der GUI

click = Button(window, text="Save password", width=20, command=speichern)
click.grid(row=12, column=2)

indicator1 = Label(window, text="If words are on, everything else is \ndeactivated", height=2, bg="light blue").grid(row=3, column=1)
ps = Label(window, text="How long should the password be?", height=2, bg="light blue").grid(row=1, column=1)

text.insert(0, "16")

empty = Label(window, bg="light blue").grid(row=9, column=1)

window.configure(background='light blue')
window.geometry("700x500")
window.title("Password generator")
mainloop()
