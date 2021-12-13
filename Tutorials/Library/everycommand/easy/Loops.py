#in python there are 2 different loops
#the first is the "while" loop

#it kinda works like a If and only stops if the content is false
a = 0
while a != 10:
    print("loop :" + str(a) + " in while")
    a += 1
#this loop is in a while with a specific statement

print("\n") #skip line

#theres another loop that works differently and simplifies for some specific purposes
#range is a special command that will be explained in another file
#this will play the loop 10 times but the loopamount will have the number inside
for loopamount in range(10):
    print("loop :" + str(loopamount) + " in for")

#in python there are specific commands for loops that works for both loop types
#for example continue and break

print("\n")

#loop that goes to 20
#normaly the variable is called "i" usualy
for i in range(20):
    if i == 5:
        #skips one loop
        continue
    print("loop : " + str(i))
    if i == 10:
        #stops entirely the loop
        break

print("\n")

#the for loop also works for lists
vegetables = ["tomato", "potato", "chili", "onion"]

for each in vegetables:
    print(each, "list loop")


print("\n")

#Note: "while 1:" will cause a loop that whouldnt stop just like "while True:"
#for loops also work for strings

potato = "potato"

for letter in potato:
    print(letter)









