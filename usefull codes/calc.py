from tkinter import *

obj = ("1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "0", "/", "**", "=", "del")

def write(info):
    if info == "=":
        calc = str(eval(userText.get()))
        userText.delete(0, len(userText.get()))
        userText.insert(1, calc)
    elif info == "del":
        userText.delete(len(userText.get())- 1, len(userText.get()))
    else:    
        userText.insert(len(userText.get()), info)

window = Tk()

userText = Entry(window, width=35)
userText.grid(row = 1, column = 1)
userText.focus_get()

for item in range(len(obj)):
    sign = obj[item]
    pos1 = item//4
    pos2 = item - pos1 * 4
    Button(window, text=str(sign), command=lambda sign = sign: write(sign), height = 5, width = 30).grid(row = pos1 + 3, column = pos2)
    

window.title("pascal made calculator")
window.mainloop()
