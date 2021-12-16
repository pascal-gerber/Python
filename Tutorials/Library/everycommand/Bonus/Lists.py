#Lists have some shortcuts like inverting a list

#the first shortcut is to create a list with integer numbers in it
Numberlist = list(range(20))

#this is a list that counts up to 20 made in one line
print(Numberlist)


#to invert a list theres 2 different way which also both work on strings

#1.
InvertedList = Numberlist[::-1] #<== this inverts the list, also works on strings
print(InvertedList)

#2.               \/ that list is needed to convert if its a string, add str
secondInverted = list(reversed(Numberlist))
print(secondInverted)


#of course you can make it a different way but these are good shortcuts
