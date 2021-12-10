#modules in python are imported, some can only be installed on the CMD
#trought specific commands

#there are a couples preinstalled modules that have some interesting functions
#we are gonna look into later

#first we want to import a simple module
#time will be one with a simple function
import time
#the syntax of imports will differ for some specific modules
#Example
from tkinter import *
#because tkinter is a very big module, it has to import everything from it.

#now the time module will allow specific commands that cannot be executed otherwise

print("start")
time.sleep(1)
print("exactly 1 second passed from start")
#this is just an example, i will be teaching you that module later
#but for now, you will have to try downloading a module from the internet

#Try openning CMD and write "python -m pip install keyboard"
#or simpler "pip install keyboard".

#it is recommanded to put "python -m" since it fixes a lot of bugs
#theres a danger that updating pip will cause it to simply deinstall
#the reason is unknown but the best way to fix it, is by
#Deinstalling python and reinstalling it all using the python installer.

#keyboard is a module we will have to loop into after

#the """ on both sides can be deleted to execute that specific command

#\/ can be deleted
"""
import os
os.system('cmd /k "python -m pip install keyboard"')
"""                                       #/\ this doesnt need to be keyboard
#/\ can be deleted                         it can be any module python has to
                                          #offer

#keyboard is just a simple module i know how to use.
#i will be explaining it later how it works.

#IMPORTANT NOTE:
#if the cmd doesn't even recognise "pip" you have to open the python installer
#and then "Modify", and select the PIP downloader.








