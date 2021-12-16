import sys
#sys - system
#a very simple and small module

#sys is mostly used for filepath management
#wierdly enought sys is made for being an extension to the Os module


#current path with python filename
print("path of the working file:", sys.argv)


#as said, Os has a very similar if not the same function.
import os
print("os version of path:", os.getcwd(), "\n\n")


#sys.path will give out a [list] with all the paths/files in the specific selected place
print("every path :\n", sys.path)


#sys.modules show how many modules and from where they are, are activated.
"print(sys.modules)"
#commented out to prevent huge data blocks

#will show what Operation system youre on
print("\n\nyour operationssystem is:", sys.platform)



sys.exit
