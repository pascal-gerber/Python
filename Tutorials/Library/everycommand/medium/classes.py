#classes are an other type of container
#classes can give multiple values to one or multiples object
#now an example, we have multiple types of cheese.
class cheese():
    content = "milk"
    #since every cheese has milk

#say camember is a cheese, so it has to be added to the cheese class
camember = cheese()

#now we can define other properties outside of the class like that
camember.typeOfCheese = "soft cheese"
#now typeOfCheese contains "soft cheese" like a normal variable

#camember has 2 values, any new object of new cheese types
#will only contain one value

print(camember.content, "camember")
print(camember.typeOfCheese, "camember")
#which whould give out both values

#now lets say theres more types of cheese
#and we got gruyere which automaticly contains
#the content already.
gruyere = cheese()

print(gruyere.content, "gruyere")
#now it whould give an error if i whould try to
#print the typeOfCheese from gruyere since
#it doesn't exist.

################################################################################
#________________________________Functions in classes___________________________

#now we add a function to a class
class hotel():
    pass

def nameNRoom(number):
    return(number.Roomnumber + " : " + number.name)
                                                # /\
#now we make a object ID containing a name as there
ID12 = hotel()
ID12.name = "Fred baumann"
    #/\ name
ID12.Roomnumber = "001"

#this will print both values in the ID12
#of course you can add new and more ID's/objects to the class.
print(nameNRoom(ID12), "||| the function itself")





















