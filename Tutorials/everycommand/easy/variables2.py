#list variable
List = ["text", 20, 3.3, True]
#a list can contain a lot of different variables
#lists have "indexes" so thier content is numbered.
#this List variables has 4 objects in it, it counts, 0, 1, 2, 3 in the index.
print(List[0])
#this will print the first object
#the number 4 whould cause an error since there isnt more than 4 objects.

#a lists content can be changed or added stuff into
List[0] = "no more text"
#this is changing the first variable
print(List[0])

#you can also print the whole list
print(List)

#to add new content to a list you use the append command
List.append("Fifth object")

#now the list should have 5 objects
print(List)

#a list can contain the same value multiples times
List.append(20)
print(List)

######################################
#there are also other variables types#
#like the tuple.                     #
######################################

#the tuple is written this way
Tuple = ("text", 20, 3.3, True)

#the tuple is "imutable" unlike the list that is
#meaning, any try to change a value or add and delete any will more cause a error than it actually changing it.
#you can test it out here
#________________________________




######################################
#other less important variables are  #
#the set and the frozenset           #
######################################

#the set is an other type of list that can be changed, except sets and frozensets can only
#contain one of any value.
Set = ({"text", 20, 3.3, True, 20, 3.3, "i am a set"})
#so we got multiples times the same value in the set

#adding stuff to a set needs to be in a list since it whould otherwise eat every letter.
Set.update(["newstuff"])
#this is the syntax of adding stuff to a set

Set.remove(3.3)
#this removes the 3.3 in the set.

print(Set)

#####################################################
#lasty we got frozenset, its just an untouchable set#
#####################################################

fset = frozenset(["text", 20, 3.3, True, 20, 3.3, "i am a frozenset"])

print(fset)

#usually set and frozenset arnt used a lot.




