from tkinter import *
import time
import threading

#creates interface on new instance
def interface():
    global window
    window = Tk()
    #the font of the window will change every font on each label or buttons
    window.option_add('*Font', '19')
    Information = Label(window, text="countdown to 2030")
    Information.grid(row=1, column=1)
    #tick...
    timeTick = Label(window, text="tick")
    timeTick.grid(row=4, column=1)
    window.title("2030 clock")
    window.geometry("700x500")
    window.mainloop()


def counter():
    global window
    TimeRemain = Label(window, text="")
    TimeRemain.grid(row=2, column=1)
    ###################################################################
    #calculates remaining time \/
    while 1:
        now = time.time()
        seconds = 1893452400 - now
        minutes = seconds//60
        seconds = seconds - (minutes * 60)
        hours = minutes//60
        minutes = minutes - (hours * 60)
        days = hours//24
        hours = hours - (days * 24)
        years = days//365
        days = days - (years * 365)
        
        #changes label every second
        countdown = str("years: " + str(int(years)) + "\ndays: "+ str(int(days)) + "\nhours: " + str(int(hours)) + "\nminutes: "+ str(int(minutes)) + "\nseconds: "+ str(int(seconds)))
        TimeRemain.configure(text=countdown)
        time.sleep(1)

#creates 2 threads
newWindow = threading.Thread(target=interface)
newWindow.start()
time.sleep(0.1)
counting = threading.Thread(target=counter)
counting.start()

	


