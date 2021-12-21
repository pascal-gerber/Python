#for manipulating strings you have some small and simple traits.
#for the first one we can skip line with \n in the middle of a string
twoLines = "hello\nworld"
                #/\ (\n)

print(twoLines, "nextline\n")

#of course there are other options

anotherLines = """hello
world"""

print(anotherLines, "nextline")

#in python there are other string manipulations types
#like putting betwem every letter or list object
#a certain letter/character in.

spaceme = "hello world"

#join simply puts a certain character of your choice
#betwem each object/letter
spacedme = "-".join(spaceme)
          #/\ this can also be a variable 

print(spacedme)

SpacemeList = ["i", "eat", "an", "apple"]

#of course it works for lists too, but it transforms
#the list into a string
spacedlist = " - ".join(SpacemeList)

print(spacedlist)



