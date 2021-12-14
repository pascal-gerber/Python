from tkinter import *

window = Tk()

###############################################################################
#_______________________Text Field_____________________________________________

BigTextField = Text(window, height=8)

#writes in the text
#Note: it also works the same syntax for "Entry" Fields
BigTextField.insert('1.0', 'Terms of service, Autor:Pascal, please learn from my tutorial')

BigTextField.grid()


###############################################################################
#_______________________Checkbutton____________________________________________

booleanVal = IntVar()
#which is the variable for checkbuttons

def FileRead():
    #since the button does that
    if booleanVal.get() == True:
        Label(window, text="you have accepted out terms of service LOL").grid()
        
        #also let us combine both
        #this takes the Texts content and makes a new label with it.
        textfield = BigTextField.get('1.0','end')
        Label(window, text=textfield).grid()
        #deletes the content in the text
        BigTextField.delete('1.0','end')

#checkbuttons are just simple buttons to be crossed and accepted
#usualy used for terms of service
Check = Checkbutton(window, text="i have read the terms of service LOL",variable=booleanVal,
                    onvalue=True, offvalue=False, #<== this writting way is legal, thanks python
                    command=FileRead)
                    #/\ works the same as button

Check.grid(row = 3, column = 0)
#row and column define height and width


window.geometry("500x500")
window.title("Guide 3")
window.mainloop()
