#math is a simple import, it doesnt require and special import
import math

##########################################################################
#math module specific

Float = 33.352

#will round up and transform the float into an integer
print(math.ceil(Float), "rounded up")

#will round down and transform the float into an integer
print(math.floor(Float), "rounded down")

#Square root
print(math.sqrt(9), ", square root")

#Greatest common divisor
print(math.gcd(50, 75), "gretest common divisor")

##########################################################################
#No module required

#round will round a number, it will round up if over 0.5
print((round(Float), 0), ", built in function")
                   #/\ Zero numbers after coma

#will transform a negative number into a positive
print(abs(-12), "positive number")

#pow and ** are the same they power up another
print(pow(9, 2), "pow power")
print(9**2, "** power")



####################
#IMPORTANT FUNCTION#
####################

#eval takes a string in a calculation syntax and executes
#the calculation
print(eval("12 * 2 + 32"), ", Eval calculation")















