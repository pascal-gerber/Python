#to open a file you need to use a methode called (open())
#open takes 2 options.
#first the file name and also the mode to open it.

#####################################################################
#Theres
#"w" = Write - will overwrite anything with the new content
#"r" = Read - will read the file if variable has .read()
#"a" = Append - will add new content as addition
#"wb" = Write binary - will write content into other types
       #of files like .exe and other in binary
#"ab" = Append binary - will append the content into
       #files as binary
#"rb" = Read binary - will read the special files binary
       #always used before anything binary
#"w+" = Write + Read - Overwrites the file but is also able
       #to read it.
#"r+" = Read + Write - Will append to the beginning new content
       #and can read the file
#"a+" = Append + Read - Will append text and read.

#"wb+" = Write binary + read binary \
#"rb+" = Read binary + write binary /
#"ab+" = Append binary + read binary
#######################################################################

#############################################################
#writting will always create a new file if non existing.
#reading will cause issues if not exisiting
#append will create new files if not existing
#############################################################


#we have to put the file in a variable
File = open("newFile.txt", "w")
                           #/\
                           #this is an option
                           #how it works is shown on top

#now the file is Writable, so we use:
File.write("hello world")
#also works on append

#to save the file you need to close it
File.close()

##############################################################
#now to read it

ReadFile = open("newFile.txt", "r")
                               #notice the r
print(ReadFile.read())

ReadFile.close()
#/\
#theres another way to write into files/read them.

#this syntax is very different since it closes after used automaticly
#and for specific needs doesn't need any options.
with open("newFile.txt") as file:
    print(file.read())

#the other with the append works like this:
    
with open("newFile.txt", "a") as file:
    file.write(" - bye world")

#lets print the content out
with open("newFile.txt") as file:
    print(file.read())





    
    




