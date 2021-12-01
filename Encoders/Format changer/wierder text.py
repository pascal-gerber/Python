import string

Ascii = ""
a = 0

while a != 75:
    Ascii += chr(a + 65296)
    a += 1

Digits = Ascii[0:10]
Upper = Ascii[17:43]
Lower = Ascii[49:75]

norDigit = string.digits
norUpper = string.ascii_uppercase
norLower = string.ascii_lowercase 

User = input("Write a text : ")

wholeText = ""

for userInput in range(len(User)):
    for Letter in range(len(Upper)):           
        if User[userInput] == " ":
            wholeText =  wholeText + "  "
            break
        try:
            if User[userInput] == norDigit[Letter]:
                wholeText = wholeText + Digits[Letter]
                break
        except:
            pass

        if User[userInput] == norLower[Letter]:
            wholeText = wholeText + Lower[Letter]
            break
        elif User[userInput] == norUpper[Letter]:
            wholeText = wholeText + Upper[Letter]
            break


print(wholeText)
input()
