#time is a simple import, small and simple
import time

while 1:
    #time.time() will give out the seconds passed since 1970 till now
    secafter1970 = time.time()
    
    #time.ctime(value) will give out the date that the value means for the code
    print(time.ctime(secafter1970))
    #note: Ctime can take values in Integer or floats.

    #time.sleep(value) will wait that value in seconds and then keep going.
    time.sleep(2)
