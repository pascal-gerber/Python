food = "pizza"

#gives out the lenght of the word as an Integer
print(len(food), ",lenght of word") 

#gives the earliest index of the word to find
print(food.find("zz"), ",find the zz") 

#makes a capital letter with every start letter of a word
print(food.capitalize(), ", capitalizing") 

#makes every letter in the string an Uppercase
print(food.upper(), ", uppercase")

#makes every letter in the string a Lowercase
print(food.lower(), ", lowercase")

#checks if its a number
print(food.isdigit(), ", its not a number")

#checks if all letters are in range of a-z
print(food.isalpha(), ", its a word with only letters")

#counts how many times the string is in the other
print(food.count("z"), ", since pizza has zz ")

#Replaces a string "commonly used"
print(food.replace("a", "eria"), ", changes a part of the string to another")

###################
#IMPORTANT TO KNOW#
###################

#strings can be also multiplied
print(food * 10, ", x10")





