#Encapsulation is making a specific type of variable in a class
class Secretname():
    #\/ this line \/ its for making an object private specificly
    def __init__(self):
        #a public takes nothing, simply defining self
        #and an object
        self.public = "Pascal"
        #the object can contain 2 lines before, making it
        #private *not accessible from outside*
        self.__private = " Secret"

    def tell():
        Secretname.__init__(Secretname)
        return(Secretname.__private)


#first name isn't private
#it works to simply print it
print(Secretname().public)

#and since the function has the return, printing it whould
#work
print(Secretname.tell())

"print(Secretname().__private)"

#/\
#|| gives out an AttributeError since it doesn't exist
