#functions are defines by "def"
#a function does specific commands when executed

#syntax of a function
def helloworld():
    print("hello world")
#this can be called as much as the user wants
    
#this is how you can call a function
helloworld()
#the name of the function and brackets, simple

#functions can have a setting inside
def printtwice(word):
#word will be the variable that holds the information
#it has been given before
    for i in range(2):
        print(word)
        #prints twice the information

#the content "twice myself" will be stored into the "word" variable
printtwice("twice myself")


#of course you will be able to give multiples settings into the
#function.

def printasmanytimes(content, number):
    for i in range(number):
        print(content)

#the syntax isnt much different
printasmanytimes("print me 3 times", 3)

#in functions we have also a "return" function in case we want it to
#become a certain value when written

def hi():
    return("hello world")
#now, printing the function itself will give out the return
#this will if the function itself is printed, print the return content
#or simply always take the return function.

print(hi())
#works for any function

