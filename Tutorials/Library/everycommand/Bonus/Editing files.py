#this function should edit files and add change to the users needs
def edit(mode, content = None):
    if mode == "w":
        with open("newFile.txt", "w+") as file:
            file.write(content)
    elif mode == "a":
        with open("newFile.txt", "a+") as file:
            file.write(content)
    elif mode == "r":
        with open("newFile.txt", "r") as file:
            return(file.read())
#/\ this could make editing a file easier


#write
edit("w", "hello")

#edit
edit("a", " world")

#read
print(edit("r"), ", which is in the txt file")
