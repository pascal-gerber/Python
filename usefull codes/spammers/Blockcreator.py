lenght = int(input("write a size number : "))
TL = "╔"
TM = "╦"
TR = "╗"
ML = "╠"
MM = "╬"
MR = "╣"
BL = "╚"
BM = "╩"
BR = "╝"
Horizontal = "║"
Vertical = "═"
contentTop = ""
contentMid = ""
contentBot = ""
Lines = ""
content = ""


for i in range(lenght):
        contentTop = contentTop + Vertical + TM
        contentMid = contentMid + Vertical + MM
        contentBot = contentBot + Vertical + BM
for e in range(lenght + 2):
        Lines = Lines + Horizontal + " "
        Mid = ML + contentMid + Vertical + MR
for f in range(lenght):
        content = content + Lines + "\n" + Mid + "\n"        

Top = TL + contentTop + Vertical + TR
Bot = BL + contentBot + Vertical + BR

print(Top + "\n" + content + Lines + "\n" + Bot)
input()