import time
from threading import Thread
def sleepFun(x):
    print("Thread ",x," is going to sleep for 2 seconds.")
    time.sleep(5)
    print("Thread ",x," is active now.")

th = Thread(target=sleepFun, args=(1, ))
th.start()
time.sleep(1)
#sleepFun(1)
print("Hello i am executing parallel to thread")
