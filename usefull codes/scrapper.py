from tkinter import * 
import re
import requests
import pyperclip
import webbrowser

find = "((https|http|\/)[^&\"\' \n]+\.(jpg|png|jpeg|jfif|exif|tiff|gif|bmp|webp|mp4|mov|wmv|flv|avi|avchd|webm|mkv))"
other = "((https|http|\/)[^&\"\' \n]+\.(ico|cs|css|js)[^&\"\' \n]*)"
discord = "(http(s)?:\/\/(discord|invite|is|kratke)\.(gg|io|me|gd|cz)\/[^&\"\' \n]*)"
twitter = "(https:\/\/twitter.com\/[^&\"\' \n]*)"
facebook = "(https:\/\/www.facebook.com\/[^&\"\' \n]*)"

VidAndPic = True
DevTool = False
DiscordInv = False
Tweets = False
FaceBook = False

#Part 2 of user Process
#________________________________________________________________________________________

def saveInFile():
    global allLinks
    nameExfiltration = userInformation.get()[8:len(userInformation.get())]
    for letter in range(len(nameExfiltration)):
        if nameExfiltration[letter] == "/":
            nameExfiltration = nameExfiltration[0:letter]
            break
    safeFile = open(nameExfiltration + ".txt", "w")
    safeFile.write(allLinks)
    safeFile.close()
    print(nameExfiltration)

def openLink(internetLink):
    webbrowser.open(internetLink)

#Part 1 of user process    
#________________________________________________________________________________________
    
def searchUp(information, linktype):
    global currentSelectedLink
    global userInformation
    global allLinks
    currentLink = ""
    allLinks = ""
    currentSelectedLink = ""
    line = 0
    height = 1
    visualLinks = re.findall(linktype, str(information))
    answer = Tk()
    Label(answer, text="open url trought button click : ")
    for element in range(len(visualLinks)):
        height += 1
        if height == 20:
            height = 1
            line += 1
        currentSelectedLink = str(visualLinks[element][0])
        if str(currentSelectedLink)[0][0] == "/":
            currentLink = userInformation.get() + currentSelectedLink
            allLinks += currentLink + "\n"
        else:
            currentLink = currentSelectedLink
            allLinks += currentLink + "\n" 
        Button(answer, text = str(currentLink),
               command = lambda openLink = openLink, currentLink = currentLink: openLink(str(currentLink)), width = 50).grid(row = height, column = line)
    Button(answer, text = "Save all links?", command = saveInFile, bg = "blue", width = 50).grid(row = 1, column = 0)
    answer.title("images and videos from link")
    answer.mainloop()

    
def scrapFile(name):
    global VidAndPic
    global DevTool
    global DiscordInv
    global Tweets
    global FaceBook
    global find
    global other
    global discord
    global twitter
    global facebook
    checkForOkay = 0
    try:
        fileItself = open(str(name), "r")
        fileContent = fileItself.read()
        fileItself.close()
        Label(window, width = 10).grid(row = 1, column = 2)
        if VidAndPic == True:
            searchUp(fileContent, find)
            checkForOkay += 1
        if DevTool == True:
            searchUp(fileContent, other)
            checkForOkay += 1
        if DiscordInv == True:
            searchUp(fileContent, discord)
            checkForOkay += 1
        if Tweets == True:
            searchUp(fileContent, twitter)
            checkForOkay += 1
        if facebook == True:
            searchUp(fileContent, facbook)
            checkForOkay += 1
        if checkForOkay == 0:
            Label(window, text="no selection actif").grid(row=3)
    except:
        error = Label(window, text = "file not found", width = 15).grid(row = 1, column = 2)
        
def findOnInternet(websiteURL):
    global VidAndPic
    global DevTool
    global DiscordInv
    global Tweets
    global FaceBook
    global find
    global other
    global discord
    global twitter
    global facebook
    try:
        htmlAllowance = requests.get(str(websiteURL))
        htmlCode = htmlAllowance.content
        if VidAndPic == True:
            searchUp(htmlCode, find)
            checkForOkay += 1
        if DevTool == True:
            searchUp(htmlCode, other)
            checkForOkay += 1
        if DiscordInv == True:
            searchUp(htmlCode, discord)
            checkForOkay += 1
        if Tweets == True:
            searchUp(htmlCode, twitter)
            checkForOkay += 1
        if facebook == True:
            searchUp(htmlCode, facebook)
            checkForOkay += 1
        if checkForOkay == 0:
            Label(window, text="no selection actif").grid(row=3)
    except:
        error = Label(window, text = "website not found", width = 15).grid(row = 1, column = 2)

#Configurations of optionnal buttons
#________________________________________________________________________________________

def VAP():
    global VidAndPic
    global videosAndPictures
    if VidAndPic == False:
        VidAndPic = True
        videosAndPictures.configure(bg = "blue")
    else:
        VidAndPic = False
        videosAndPictures.configure(bg = "white")

def DEV():
    global DevTool
    global DevelopperUse
    if DevTool == False:
        DevTool = True
        DevelopperUse.configure(bg = "blue")
    else:
        DevTool = False
        DevelopperUse.configure(bg = "white")

def DISC():
    global DiscordInv
    global DiscordLinks
    if DiscordInv == False:
        DiscordInv = True
        DiscordLinks.configure(bg = "blue")
    else:
        DiscordInv = False
        DiscordLinks.configure(bg = "white")

def TWITT():
    global Tweets
    global TwitterLinks
    if Tweets == False:
        Tweets = True
        TwitterLinks.configure(bg = "blue")
    else:
        Tweets = False
        TwitterLinks.configure(bg = "white")

def Facebook():
    global FaceBook
    global FacebookLinks
    if FaceBook == False:
        FaceBook = True
        FacebookLinks.configure(bg = "blue")
    else:
        FaceBook = False
        FacebookLinks.configure(bg = "white")    

#generation of first window
#________________________________________________________________________________________

def generateLayout():
    global userInformation
    global videosAndPictures
    global DevelopperUse
    global DiscordLinks
    global TwitterLinks
    global FacebookLinks
    Label(window, text = "write a filePath or a URL here").grid(row = 1, column = 1)
    userInformation = Entry(window)
    userInformation.grid(row = 2, column = 1)
    userInformation.focus_set()
    fileScrapp = Button(window, text = "click to\nresearch a file",
                        command = lambda scrapFile = scrapFile: scrapFile(userInformation.get()), bg = "green",
                        height = 3, width = 15)
    fileScrapp.grid(row = 3, column = 1)
    webScrapp = Button(window, text = "click to\nresearch the web",
                        command = lambda findOnInternet = findOnInternet: findOnInternet(userInformation.get()), bg = "green",
                        height = 3, width = 15)
    webScrapp.grid(row = 3, column = 2)
    Label(window).grid(row = 4)
    videosAndPictures = Button(window, text = "Videos and pics", command=VAP, height = 3, width = 22, bg = "blue")
    videosAndPictures.grid(row = 5, column = 1)
    DevelopperUse = Button(window, text = "Developper tool", command=DEV, height = 3, width = 22, bg = "white")
    DevelopperUse.grid(row = 5, column = 2)
    DiscordLinks = Button(window, text = "Discord links", command=DISC, height = 3, width = 22, bg = "white")
    DiscordLinks.grid(row = 5, column = 3)
    TwitterLinks = Button(window, text = "Twitter links (non functionnal yet)", command=TWITT, height = 3, width = 22, bg = "white")
    TwitterLinks.grid(row = 6, column = 1)
    FacebookLinks = Button(window, text = "Facebook links", command=Facebook, height = 3, width = 22, bg = "white")
    FacebookLinks.grid(row = 6, column = 2)
    
window = Tk()

generateLayout()


window.title("Scrapper")
window.geometry("500x500")
window.mainloop()
