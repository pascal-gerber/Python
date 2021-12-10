#the time module is a very helpfull module that has a lot of different functions
#the most used function in time is: time.sleep(which just waits).
import time
#time doesn't need any specific import.
#a simple import does the trick.

#now lets start with a small programm that counts up automaticly by date
#its simple and uses a lot of the time module.

for i in range(20):
    #time.time() will give out the seconds that have passed since 1970 till now
    seconds = time.time()
    #time.ctime(sec) will take that number and convert it into a date
    datetime = time.ctime(seconds)
    #now datetime got the date in a string template
    print(datetime)
    #now we want it to print the time every second.
    time.sleep(1)
    #time.sleep() will wait the amount of time has been set into the parameter
    break
    #you can remove the "break" command to see its full function

    #########################################
    #Little details -not important to know- #
    #########################################

#in the time module we got another type of syntax for the date

now = time.gmtime(time.time())
#the now became something like a dictionnary
#it can spit out any number if asked

#all the number types you can ask are here:
#tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday
#tm_yday, tm_isdst

print(now.tm_year)

#the mktime takes another type of list

randomdata = (2021,  12,   28,    8,  44,   4,    4,  362, 0)
             #year, mon, mday, hour, min, sec, wday, yday, isdst

returntosec = time.mktime(randomdata)
#will give out the seconds in it
print(time.ctime(returntosec))







