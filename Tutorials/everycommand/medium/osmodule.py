import os
#the os module has a simple import

#os has a lot to do with paths.
#but os has other functions too

#the first function that is used early in progrmaming
#python is the "cmd" controll with the os.
"""
os.system('cmd /k "Your Command Prompt Command"')
"""           #/\ /k continues after
              #|| if /c, will terminate after

#this is gonna be able to be executed on your CMD.
#it has some very usefull functions.

#some other functions that you might need have to do
#with filepaths.

#so to know where the file is at, we can write
path = os.getcwd()
#path contains there place where the file is at.
print(path)
#this is a string containing the path where the file is at

#to see all the other files, you can write "os.listdir()"

print(os.listdir(path))
#the path can be given and it will show any file in it.

#theoreticly you can use os to search the whole PC
#with specific filenames.

#programs using OS will be in the Project section
#this is just the basics
