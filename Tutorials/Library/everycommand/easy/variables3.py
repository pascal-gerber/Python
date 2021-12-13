#variables can be transformed in some degree
String = "1"
#this string can be anything of the 4 single variable types

print(type(String), "string")
#but for now its a string

#lets tranform the String into an integer
Integer = int(String)
#the integer is now the strings value

print(type(Integer), "integer")

#there are other changes we can do like
Float = float(String)
Float = float(Integer)
#since the 2 have the same value, they can be both transformed.
#both will do the same result

print(type(Float), "float")

#python doesnt care what type it converts.
Boolean = bool(Integer)
Boolean = bool(String)
Boolean = bool(Integer)

print(type(Boolean), "boolean")

#tho python doesnt care, you need to be carefull also to sometimes translate the right way
option1 = str(Boolean)
option2 = str(int(Boolean))

print(option1, "string directly")
print(option2, "int, then string")
#same value, other result.

#################################
#it also works for list types of#
#variable types                 #
#################################

List = ["hello", 20, 3.3, True]

print(type(List), "the list")

Tuple = tuple(List)

print(type(Tuple), "the tuple")

Set = set(List)

print(type(Set), "the set")

Fset = frozenset(List)

print(type(Fset), "the frozenset")

#same here, python can without a problem, convert em to the variables it wants





