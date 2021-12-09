#Indexes have a lot of different ways to be written

#indexes start always with index 0, Every object has indexes.
Fruits = ["orange", "apple", "pineapple"]
#         index 0 , index 1 , index 2

Onefruit = "Pineapple"

#this is index 1
print(Fruits[1], ", index 1 of list 'Fruits'")

#the same concept works with strings
print(Onefruit[1], ", second letter from word")

#we can add 2 options into the index link.

#-2 is when taken from the end
print(Onefruit[2: -2], "both defined")

#if only one option given, the rest will be to one end
print(Onefruit[4:], "start defined")

print(Onefruit[:4], "end defined")

#theres also a thirt option
#skips letters
print(Onefruit[::2], "Pnape")
#that last 2 skips one of 2 letters

#of course this can be used for reversing
print(Onefruit[::-1], "reverse string")

#the index is a "slice" object

Index = slice(4, 7)

#indexes can still contain up to 3 informations.
print(Onefruit[Index])

