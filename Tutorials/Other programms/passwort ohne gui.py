import random
import string
import datetime

choice = string.ascii_lowercase

full = ""
#full ist das ganze passwort

lenght = input("wie lang soll das passwort sein? (wenn leer 16) : ")
numbers = input("soll das password nummern enthalten? y/ignore : ")
big = input("soll das password Grosse Buchstaben enthalten? y/ignore : ")
signs = input("soll das password zeichen enthalten? y/ignore : ")
file = input("wilst du eine datei ? name/ignore : ")
#fragen zu dem user

if len(lenght) == 0:
    lenght = 16
if numbers == "y":
    choice = choice + str(string.digits)
if big == "y":
    choice = choice + str(string.ascii_uppercase)
if signs == "y":
    choice = choice + str(string.punctuation)
#functionnen zu den fragen

for i in range(int(lenght)):
        full = full + choice[random.randint(0, len(choice) - 1)]
#generieren des passwortes

if len(file) > 0:
    data = open(str(file) + ".txt", "w")
    data.write(full + "\n\nCreated at :\n" + str(datetime.datetime.now()))
    data.close()
#speichern des passwortes

print(full)
