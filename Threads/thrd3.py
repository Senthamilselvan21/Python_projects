import time
from threading import Thread
def eventhrd(x,y):
    print("Even thread executing")
    time.sleep(5)
    print("ex is:",x)
def oddthrd(y):
    print("Odd thread executing")
    time.sleep(10)
    print("ox is:",y)
th = Thread(target=eventhrd, args=(1,4))
th.start()
time.sleep(1)
th1 = Thread(target=oddthrd, args=(1,))
th1.start()
time.sleep(1)
#sleepFun(1)
