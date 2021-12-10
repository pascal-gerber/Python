#input fields are here to take user Inputs in the comandboard
name = input("what's your name : ")

#inputs will be stored in a variable.
#and can be customized to hold any type of variables

age = int(input("how old are you? : "))

#it acts just like a string
print(type(input("Random text here(its always a string): ")))

#of course for strings there are other ways to connect multiples strings
#option 1
print("your name is", name, "and you're", age, "years old")

#option 2
print("your name is " + name + " and you're " + str(age) + " years old")

#of course theres more but i dont think you'l ever ever gonna need em.
