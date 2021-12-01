while 1:
    userText = input("Write a text to decode : ")

    Text = userText[0:-2]
    wholeText = ""

    removedFirst = str(ord(userText[-2]))
    removedSecond = str(ord(userText[-1]))

    Divident = (removedFirst[2:len(removedFirst)])
    Substraction  = (removedSecond[2:len(removedSecond)])

    for i in range (len(userText) - 2):
        wholeText += chr((ord(userText[i]) - int(Substraction)) // int(Divident))
                         
    print(wholeText)
