import os

#Getting path
print(os.getcwd())

#changing path
os.chdir("F:\\")

#seing the change
print(os.getcwd())
#str

#seing all the paths
print(os.listdir())
#list

#unknown
print(os.name)

#writes in CMD
"""
os.system('cmd /k "Your Command Prompt Command"')
"""           #/\ /k continues after
              #|| if /c, will terminate after

