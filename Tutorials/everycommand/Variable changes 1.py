#there are some specific words that do specific command
#like join for example:

countries = ["france", "switzerland", "germany", "italy"]

#this print is gonna make a type string with the list
print(",".join(countries))
#the coma before the join is the string it should build in
#betwem every list object
#Note: it can be any signs or text at the coma part

bigString = (",".join(countries))

print(type(bigString))
#is it the same as the print basicly.

#the opposite of "join" is "split".
#it takes a string and transforms it into a list by
#cutting where the sign apears.

#it will cut the list by every comma.
print(bigString.split(","))

#the syntax to put it in a variable is:
newListVariable = bigString.split(",")

#the type is a List afterwarts
print(type(newListVariable))
