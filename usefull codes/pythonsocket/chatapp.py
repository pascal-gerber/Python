import socket
import threading
from tkinter import *

userNumb = 1

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
    global newchatwindow
    global user
    newchatwindow = Tk()
    newchatwindow.geometry("800x800")
    newchatwindow.title("Server ID " + str(user.get()))
    newchatwindow.mainloop()

def waitForMessage():
    global connect
    global temp
    global str_recv
    global chatpage
    global userNumb
    str_recv, temp = connect.recvfrom(1024)
    message = str(str_recv).split("'")
    Label(chatpage, text=("user" + str(userNumb) + " :" + str(message[1]))).grid()
    Label(newchatwindow, text=("user" + str(userNumb) + " :" + str(message[1]))).grid()


def waitfornew():
    global connect
    global s
    global Chatpage
    global Server
    global connect
    global userNumb
    newwindow = threading.Thread(target=Createdserver)
    newwindow.start()
    connect, addr = s.accept()
    Label(Server, text="Joined address : " + str(addr)).grid()
    Label(newchatwindow, text="user" + str(userNumb) + " has joined").grid()
    while 1:
        waitForMessage()
    
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
        try:
            if Butt == 1:
                Join = threading.Thread(target=JoinServer(UserInput))
                Join.start()
            else:
                Create = threading.Thread(target=createServer(UserInput))
                Create.start()
        except:
            Label(window, text="Input must be 4 Numbers or server must exist").grid(row=4, column=1)


createWindow = threading.Thread(target=createWindow())
createWindow.start()

