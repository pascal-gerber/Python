from tkinter import *
import time
import threading
    
def interface():
    global window
    window = Tk()
    window.option_add('*Font', '19')
    Information = Label(window, text="this deceased world will no longer be free thanks to humans: enjoy the doomsclock to evil plans")
    Information.grid(row=1, column=1)
    timeTick = Label(window, text="time is ticking")
    timeTick.grid(row=4, column=1)
    window.title("Doom clock")
    window.geometry("700x500")
    window.mainloop()


def counter():
    global window
    TimeRemain = Label(window, text="")
    TimeRemain.grid(row=2, column=1)
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
        Problem = str("years: " + str(int(years)) + "\ndays: "+ str(int(days)) + "\nhours: " + str(int(hours)) + "\nminutes: "+ str(int(minutes)) + "\nseconds: "+ str(int(seconds)))
        TimeRemain.configure(text=Problem)
        time.sleep(1)

newWindow = threading.Thread(target=interface)
newWindow.start()
time.sleep(0.1)
counting = threading.Thread(target=counter)
counting.start()

	


