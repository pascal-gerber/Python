#The if command only works with booleans.
if True:
    print("the true is on")

#but the true can be archieved differently
print(1 < 2, " <= this is true")
#1 is smaller than 2, which is true
#python is gonna print out true

#false works the same
print(2 < 1, " <= this is false")

print("test")
#now lets put it all into a if statement
if 1 < 2:
    print("this is True")

#now we sometimes got momments where we want it to do something but if it
#doesnt work, to do something else

#####################################

if 1 > 2:
    print("this whould be true")
#the else command never needs any indication and only works after an if
#the else will activate if the if command isnt.
else:
    print("this if is false")

#####################################

#now we also got momments where we wanna check if something is another way.
#basicly another if in the sentance
a = 2

if a == 1:
    print("the first if works")
#elif works as "else if" it will work if its true and the if is false tho.
elif a == 2:
    print("the second if works")
#we can always put an if as a failsafe.
else:
    print("failsafe")

#the statements exists also in different statement ways.

######################################

#true if same value
print(2 == 2, "<= same value '=='")
#true if only bigger
print(2 > 1, "<= bigger '>'")
#true if bigger or same
print(2 >= 1, "<= bigger or same '>='")
#true if only smaller
print(1 < 2, "<= smaller '<'")
#true if smaller or same
print(1 <= 2, "<= smaller or same '<='")
#true if not the same
print(1 != 2, "<= not the same '!='")

############################################

#is works like ==, its a python word
print(1 is 1, "we used the is to make a True 'works like =='")

#we can also use other words like "and" and "or"
print(1 == 1 and 2 == 2, "which is using an and")
print(1 == 2 or 2 > 1, "which is an or")

#of course theres another way you can write the and as well to make things shorter
if 1 < 2 == 2 < 3:
    print(2 + 2 == 4 < 5 < 6, "the long calculation part")
#you can mix multiples conditions into one long condition

#funny code you can make
if True is not False:
    print(False is not True, "<= false is not true")
#reflects to \/
#if True != False:
    #print(True != False)















