import time
from threading import Thread
def sleepFun(x):
    print("Thread ",x,"is going to sleep for 5 seconds")
    time.sleep(5)
    print("Thread ",x," is active now.")
th=Thread(target=sleepFun,args=(1, )) # defining function in thread
th.start() #set starting time
time.sleep(3) #set sleeping time
#sleepFun(1)
print("Hello i am executing parallel to thread")