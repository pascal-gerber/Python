import random

while 1:
    userText = input("Write a text to encode : ")
    userMult = str(random.randint(10,99))
    userAddition = str(random.randint(10,99))

    endAddition = ""

    if len(userMult) == 0:
        userMult = 1
    endAddition += chr(int("10" + str(userMult)))
    if len(userAddition) == 0:
        userAddition = 0
    endAddition += chr(int("20" + str(userAddition)))

    wholeText = ""
    signsAndNumbers = ""

    userFactor = "*" + str(userMult) + "+" + str(userAddition)

    for i in userText:
        wholeText += (chr(int(eval(str(ord(i)) + str(userFactor)))))

    print(wholeText + endAddition)
        
    try:
            import pyperclip
            pyperclip.copy(wholeText + endAddition)
            print("\n your message has been copied on clipboard")
    except:
            print("\n no extension active (Copy manualy)")
    
