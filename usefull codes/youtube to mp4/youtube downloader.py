from tkinter import *
import youtube_dl
from youtube_dl import YoutubeDL
import threading

def checkInput():
    global youtubeLink
    global filename
    global process
    ILink = youtubeLink.get()
    VName = filename.get().lower()
    if len(youtubeLink.get()) != 0 and len(filename.get()) != 0:
        downloadProc = threading.Thread(target=lambda ILink = ILink, VName = VName: download(ILink, VName))
        downloadProc.start()
        process.configure(text="downloading :" + ILink + "\nas " + VName)
    else:
        process.configure(text="Incorrect input")
            
def createInterface():
    global youtubeLink
    global filename
    global process
    window = Tk()
    Label(window, text="Youtube link here").grid(row=1, column=1, columnspan=3)
    youtubeLink = Entry(window)
    youtubeLink.grid(row=2, column=1)
    Label(text="Write the name of the file it should be saved as\nincluding the type \".mp3\", \"mp4\", \".mov\", \".m4a\"").grid(row=3, column=1)
    filename = Entry(window)
    filename.grid(row=4, column=1)
    confirm = Button(window, text="confirm download", command=checkInput)
    confirm.grid(row=8, column=1)
    process = Label(window, height = 5, width = 60, text="Nothing")
    process.grid(row = 10, column = 1)
    window.title("youtube downloader")
    window.geometry("500x500")
    window.mainloop()

def download(Link, name):
    global process
    sound = False
    video = False
    if name[-3:len(name)] == "mp3" or name[-3:len(name)] == "m4a" or name[-3:len(name)] == "wav":
        sound = True
    elif name[-3:len(name)] == "mp4" or name[-3:len(name)] == "mov":
        video = True
        
    if sound == True:
        options={'format':'bestaudio',
                 'keepvideo':False,
                 'outtmpl':name, }
    elif video == True:
        options={'format':'bestvideo',
                 'keepvideo':False,
                 'outtmpl':name,}
    else:
        process.configure(text="Incorrect input")
        
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([Link])

createInterface()
