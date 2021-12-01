class privatestuff():
    def giveout():
        #if in the name theres a underline, that variable will only be accessible from inside the class.
        _privatename = "pascal"
        return(_privatename)


#since this isnt inside the class, it will cause an error
"""
print(_privatestuff)
"""

#this gives out the value since theres a function that gives it out
print(privatestuff.giveout())

