while 1:
    text = input("Write a text to decode : ")
    dec = ""
    whole = ""
    
    for i in text:
        dec = str(ord(i))
        if(len(dec) <= 3):
            whole += (chr(int(dec)))
        elif(int(dec[0:3])) < 122:
            whole += ((chr(int(dec[0:3]))) + chr(int(dec[3:len(dec)])))
        elif(int(dec[0:2])) > 23:
            whole += ((chr(int(dec[0:2]))) + chr(int(dec[2:len(dec)])))
        
        whole = whole.replace("cα", "zX-")
        whole = whole.replace(":comet:", "a ")
        whole = whole.replace(":writing_hand:", "ca")
        whole = whole.replace(":arrow_upper_left:", "Ub")
        whole = whole.replace(":hotsprings:", "b ")
        whole = whole.replace(":star_and_crescent:", "aF")
        whole = whole.replace(":sparkle:", "d7")
    print(whole)
