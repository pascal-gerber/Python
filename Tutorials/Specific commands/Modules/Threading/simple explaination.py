#time is the problem module since it can only work in one instance
import time
#threading fixes that issue
import threading 


#we have 2 classes that interfere in each other*
def first():
    for i in range(3):
        time.sleep(1)
        print("Hello")
        
def second(): 
    for i in range(3):
        time.sleep(1)
        print("Hi") 
#______________________________________________*

#you have to define a thread first before you can execute it.
t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)  


#these commands will start both threads in each other.
t1.start()
time.sleep(0.1)
t2.start()
