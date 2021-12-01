import random

first = ["this ", "file ", "is ", "very ", "large "]

new = open("giant.txt", "w")

longstring = ""

for i in range(10000):
    for string in range(1000):
        longstring += random.choice(first)
    new.write(longstring)
    longstring = ""
    
new.close()
