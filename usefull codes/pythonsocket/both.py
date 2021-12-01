import socket
import threading
from tkinter import *

connect = 0.0

def createWindow():
    global window
    global user
    window = Tk()
    user = Entry(window)
    user.grid(row=1, column=1)
    user.focus_get()
    Button(window, text="Join IP Server", command=lambda user = user:check4Numbers(user.get(), 1)).grid(row=2, column=1)
    Button(window, text="Create Server under IP", command=lambda user = user:check4Numbers(user.get(), 2)).grid(row=2, column=2)
    window.geometry("800x800")
    window.mainloop()

def chat():
    global Chatpage
    global user
    Chatpage = Tk()
    Chatpage.geometry("800x800")
    Chatpage.title("Server ID " + str(user.get()))
    Chatpage.mainloop()

def waitForMessage():
    global connect
    global temp
    global str_recv
    str_recv, temp = connect.recvfrom(1024)
    print(str_recv)


def waitfornew():
    global connect
    global s
    global Chatpage
    global Server
    global connect
    newwindow = threading.Thread(target=Createdserver)
    newwindow.start()
    connect, addr = s.accept()
    Label(Server, text="Joined address : " + str(addr)).grid()
    Label(Chatpage, text="A new user has joined").grid()
    while 1:
        waitForMessage()
    print("first")
    
def Createdserver():
    global Server
    Server = Tk()
    Server.title("Joined IP")
    Server.mainloop()

def createServer(IP):
    global connect
    global addr
    global s
    global window
    global connect
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('localhost', int(IP)))
    
    s.listen(5)
    flag = 0
    
    waitforusers = threading.Thread(target=waitfornew)
    waitforusers.start()

    newChatPage = threading.Thread(target=chat)
    newChatPage.start()
        
    Label(window, text="server created").grid(row=5, column=1)

#____________________________________________________________________________

def userchat():
    global chatpage
    global chatEntry
    global user
    chatpage = Tk()
    chatEntry = Entry(chatpage)
    chatEntry.grid(row=1, column=1)
    chatEntry.focus_get()
    waitingForText = threading.Thread(target= waitForText)
    waitingForText.start()
    Button(chatpage, text="send =>", command=sendMessage).grid(row=1, column=2)
    chatpage.geometry("500x500")
    chatpage.title("chatroom ID" + user.get())
    chatpage.mainloop()

def sendMessage():
    global str_recv
    global so
    global chatEntry
    str_send = chatEntry.get()
    so.send(bytes(str_send, 'utf-8'))


def waitForText():
    global chatpage
    global so
    str_recv = so.recv(1024)
    print("second")
    print(str(str_recv))

    

def JoinServer(IP):
    global str_recv
    global so
    
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    so.connect(("localhost", int(IP)))

    createChatWindow = threading.Thread(target=userchat)
    createChatWindow.start()

def check4Numbers(UserInput, Butt):
    global window
    if len(UserInput) == 4:
        #try:
            if Butt == 1:
                Join = threading.Thread(target=JoinServer(UserInput))
                Join.start()
            else:
                Create = threading.Thread(target=createServer(UserInput))
                Create.start()
                createServer(UserInput)
        #except:
            #Label(window, text="Input must be 4 Numbers or server must exist").grid(row=4, column=1)

createWindow = threading.Thread(target=createWindow())
createWindow.start()

