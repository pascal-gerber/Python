#in tkinter theres another way to write programms which i don't really encourage to use.
import tkinter as tk
#now we see how it is different from the from tkinter import *

#personnaly it is quite messy to import as tk.
window = tk.Tk()
        #/\ tk.

#before any object on the window, you always have to write tk. at the start

tk.Label(window, text="tk. is at the start").grid()
#/\ its easier without
#and also less messy

#so we return to the better version

from tkinter import *

#this is how to properly write objects
Newlabel = Label(window, text="nothing is behind")
Newlabel.grid()

#now for buttons with options inside the command you need to use lambda.
#lambda is a simple bugfix that in some situations will solve issues.

Number = 10

def clicked(objects):
    Label(window, text=objects).grid()


clickMe = Button(window, text="click me",
                 command=lambda Number = Number: clicked(Number)) #important lambda function
clickMe.grid()          #/\                   /\ this whole part belongs to lambda
#                        lambda Number = Number: it is needed to define that changing parameter
#                                                into a changing constant.

#######################################
#this was it with the Tkinter tutorial#
#######################################






























#you've found it!
Problem = """
      ___ ___  ___  ___ _    ___ __  __   ___  ___  _ __   _____ _  _  ___
     | _ \ _ \/ _ \| _ ) |  | __|  \/  | / __|/ _ \| |\ \ / /_ _| \| |/ __|
     |  _/   / (_) | _ \ |__| _|| |\/| | \__ \ (_) | |_\ V / | || .` | (_ |
     |_| |_|_\\___/|___/____|___|_|  |_| |___/\___/|____\_/ |___|_|\_|\___|
                         ___ ___  ___   ___ ___ ___ ___
                        | _ \ _ \/ _ \ / __| __/ __/ __|
                        |  _/   / (_) | (__| _|\__ \__ \
                        |_| |_|_\\___/ \___|___|___/___/

                    YES   =============================   NO
             +-----------|| Does the Darn Thing work? ||-----------+
             |            =============================            |
             V                                                     V
        +----------+     +---------+                          +---------+
        |   Don't  |  NO |   Does  |       +-------+     YES  | Did you |
        |   mess   | +---|  anyone |<------|  YOU  |<---------|   mess  |
        | with it! | |   |  know?  |       | MORON |          | with it |
        +----------+ |   +---------+       +-------+          +---------+
             |       V        | YES                                |  NO
             |    +------+    +-----------+                        |
             |    | HIDE |                V                        V
             |    |  IT  |            +--------+             +-----------+
             |    +------+            |  YOU   |        YES  | WILL THEY |
             |       |       +------->|  POOR  |<------------| CATCH YOU?|
             |       |       |        |BASTARD!|             +-----------+
             |       |       |        |________|                   |  NO
             |       |       |             |                       |
             |       |       |             V                       V
             |       |       |      +---------------+        +-----------+
             |       |       |  NO  | CAN YOU BLAME |        |DESTROY THE|
             |       |       +------| SOMEONE ELSE? |        |  EVIDENCE |
             |       |              +---------------+        +-----------+
             |       |                     |  YES                  |
             |       |                     v                       |
             |       |      ============================           |
             |       +---->||           N O            ||<---------+
             +------------>||      P R O B L E M       ||
                            ============================
"""







