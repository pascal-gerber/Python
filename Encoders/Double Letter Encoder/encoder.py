while 1:
        User = input("write a text to Encode : ")
        e = ""
        t = 0
        z = ""
        User = User.replace("zX", "ϧ")     
        for i in User:
                if t == 0:
                        e = e + str(ord(i))
                        t = 1
                else:
                        e = e + str(ord(i))
                        t = 0
                        z = z + chr(int(e))
                        e = ""
                
        if (len(User)%2) == 1:
                z = z + User[-1]
                
        print(z + " |")

        try:
                import pyperclip
                pyperclip.copy(z)
                print("\n your message has been copied on clipboard")
        except:
                print("\n no extension active (Copy manualy)")
