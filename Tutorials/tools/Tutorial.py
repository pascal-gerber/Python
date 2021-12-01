from tkinter import *

objects = []
currentPage = 0
maxPages = 10

congrats = ""

#_________________________________________________________________________________________________________

def firstPage():
    global objects
    global currentPage
    global userEntry
    global ValidationButton
    firstText = "Lets start with a Hello World:\nPrint function gives out a text such as\nprint(\"hello world\")"
    textLabel = Label(window, text=firstText)
    textLabel.grid(row=1, column=2, rowspan = 5, columnspan = 5)
    objects.append(textLabel)
    userEntry = Entry(window)
    userEntry.grid(row=2, column=2, rowspan = 5, columnspan = 5)
    userEntry.focus_get()
    objects.append(userEntry)
    ValidationButton = Button(window, text="Validate", command=lambda Validate = Validate, currentPage = currentPage: Validate(currentPage))
    ValidationButton.grid(row=7, column=2, rowspan = 5, columnspan = 5)
    objects.append(ValidationButton)

def secondPage():
    global objects
    firstText = "Variables can be used in commands like print()\nexample: print(b)\nwhich prints the value of b.\na value is defined simply by writting:\n a = 5\nb = a"
    textLabel = Label(window, text=firstText)
    textLabel.grid(row=2, column=2, rowspan=5, columnspan=7)
    objects.append(textLabel)

def thirthPage():
    global objects
    firstText = "you can add variables togheter and depends on the type of variable it will give different results.\n but first you need to learn what a \"variabletype\" is\n\n"
    secondText = "String - str (is text, whould make 2 + 2 = 22)\nInteger - int (is a number, whould make 2 + 2 = 4)\nDecimal Number - float (is a decimal Number, whould make 2 + 2 = 4.0)\nBoolean - bool (can be True or False.)"    
    textLabel = Label(window, text=firstText + f'{secondText : <10}', anchor='e')
    textLabel.grid(row=0, column=0, rowspan=10, columnspan=10)
    objects.append(textLabel)
    window.geometry()

def fourthPage():
    global objects
    global currentPage
    global userEntry
    global ValidationButton
    firstText = "You can convert a Integer to a String or anything else by putting the shortword for the type\n<- see previous page\n\nYou can convert easly in python using commands like\nint(b) or str(b).\n\nMake a New Variable named \"c\" that has the same Value as \"b\" but as a string.\n"
    textLabel = Label(window, text=firstText)
    textLabel.grid(row=1, column=0, rowspan=10, columnspan=10)
    objects.append(textLabel)
    userEntry = Entry(window)
    userEntry.grid(row=5, column=2, rowspan=5, columnspan=5)
    userEntry.focus_get()
    objects.append(userEntry)
    ValidationButton = Button(window, text="Validate", command=lambda Validate = Validate, currentPage = currentPage: Validate(currentPage))
    ValidationButton.grid(row=7, column=2, rowspan = 5, columnspan = 5)
    objects.append(ValidationButton)

def fiftPage():
    global objects
    textLabel = Label(window, text="There are Certain things you have to convert multiples times like for example :\nstr(int(True))\n\nWhich is tranforming a Boolean into an integer then into a string.\nit whould be a different result if it was changed immediatly into a string.")
    textLabel.grid(row=0, column=0, rowspan=10, columnspan=10)
    objects.append(textLabel)

def sixthPage():
    global objects
    textLabel = Label(window, text="Changing from Variables we have \"if\" functions.\nan if function is for Comparing variables or generally seing if a statement is true.\nWith these functions, try thinking its a language in real life. Example;\n\n\"if\" you drive a car straight you end up in Bern\n\"else if\" you go to the left you end up in Thun\n\"else\" you go to Ostermundigen\n\nbut as \"if\", \"elif\" and \"else\"")
    textLabel.grid(row=0, column=0, rowspan=10, columnspan=10)
    objects.append(textLabel)

def seventhPage():
    global objects
    textLabel = Label(window, text="In the if functions there are comparing signs betwem 2 Values\n\n\"==\" is true if both are on the same value\n\"<\" is smaller than\n\">\" is bigger than\n\"!=\" is true if both arnt the same\n\"<=\" is smaller or the same\n\">=\" is bigger or the same")
    textLabel.grid(row=0, column=0, rowspan=10, columnspan=10)
    objects.append(textLabel)

def eigthPage():
    global objects
    global currentPage
    global userEntry
    global ValidationButton
    textLabel = Label(window, text="If function only turn on when thier content is true, otherwise they whould not activate.\n\nexample: \"if a > b:\"\n\nwrite a function that only activates if c is the same as b")
    textLabel.grid(row=0, column=0, rowspan=10, columnspan=10)
    objects.append(textLabel)
    userEntry = Entry(window)
    userEntry.grid(row=4, column=2, rowspan = 5, columnspan = 5)
    userEntry.focus_get()
    objects.append(userEntry)
    ValidationButton = Button(window, text="Validate", command=lambda Validate = Validate, currentPage = currentPage: Validate(currentPage))
    ValidationButton.grid(row=7, column=2, rowspan = 5, columnspan = 5)
    objects.append(ValidationButton)

def ninthPage():
    global objects
    textLabel = Label(window, text="working on")
    textLabel.grid(row=1, column=0, rowspan = 1, columnspan = 5)
    objects.append(textLabel)

def tenthPage():
    global objects
    textLabel = Label(window, text="working on")
    textLabel.grid(row=1, column=0, rowspan = 1, columnspan = 5)
    objects.append(textLabel)

#________________________________________________________________________________________________________

def Validate(page):
    global userEntry
    global objects
    global congrats
    global ValidationButton
    if page == 1 and userEntry.get() == "print(\"hello world\")" or userEntry.get() == "print(\"Hello world\")":
        ValidationButton.config(text="Well done!", state='disabled')
    elif page == 4 and userEntry.get() == "c = str(b)" or userEntry.get() == "c=str(b)":
        ValidationButton.config(text="Well done!", state='disabled')
    elif page == 8 and userEntry.get() == "if c == b:" or userEntry.get() == "if b == c:":
        ValidationButton.config(text="Well done!", state='disabled')

def createInterface():
    global pageNumber
    global objects
    global window
    tutorialwelcome = Label(window, text="Hello user, this is a Python tutorial\nMade by Pascal\nEnjoy")
    tutorialwelcome.grid(row=1, column=2, rowspan=5, columnspan=5)
    objects.append(tutorialwelcome)

def checkPageNumber(Dir):
    global currentPage
    global maxPages
    global pageDown
    global pageUp
    global objects
    
    for each in objects:
        each.destroy()
    
    if currentPage == 1 and Dir == "Down":
        pageDown.config(state='disabled')
    else:
        pageDown.config(state='normal')
        
    if currentPage == (maxPages -1) and Dir == "Up":
        pageUp.config(state='disabled')
    else:
        pageUp.config(state='normal')

    if Dir == "Up":
        showPage.config(text="page: " + str(currentPage + 1))
    else:
        showPage.config(text="page: " + str(currentPage - 1))
    
    
def pageOneUp():
    global currentPage
    checkPageNumber("Up")
    currentPage += 1
    pageUpdate(currentPage)

def pageOneDown():
    global currentPage
    checkPageNumber("Down")    
    currentPage -= 1
    pageUpdate(currentPage)

def pageUpdate(nowerdaypages):
    global window
    if nowerdaypages == 0:
        createInterface()
    elif nowerdaypages == 1:
        firstPage()
    elif nowerdaypages == 2:
        secondPage()
    elif nowerdaypages == 3:
        thirthPage()
    elif nowerdaypages == 4:
        fourthPage()
    elif nowerdaypages == 5:
        fiftPage()
    elif nowerdaypages == 6:
        sixthPage()
    elif nowerdaypages == 7:
        seventhPage()
    elif nowerdaypages == 8:
        eigthPage()
    elif nowerdaypages == 9:
        ninthPage()
    elif nowerdaypages == 10:
        tenthPage()
        






window = Tk()
for i in range(10):
    naturalMargin = Label(window, height=3, width=5).grid(row = i, column = 0)
for i in range(10):
    naturalMargin = Label(window, height=3, width=5).grid(row = 0, column = i)
pageDown = Button(window, text="<- page back", command=pageOneDown, state='disabled')
pageDown.grid(row=i-1, column = 0)
pageUp = Button(window, text="page forward ->", command=pageOneUp)
pageUp.grid(row=i-1, column = i)
showPage = Label(window, text="page: " + str(currentPage))
showPage.grid(row=9, column = 0, columnspan=10)

createInterface()

window.title("Python tutorial")
window.geometry("520x500")
window.mainloop()
