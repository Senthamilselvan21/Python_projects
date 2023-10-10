import time
from threading import Thread

def calculation():
	a=10
	b=20
	res=a+b
	return res
def sleepFun(x):
    print("Thread ",x," is going to sleep for 20 seconds.")
    time.sleep(20)
    print("Thread ",x," is active now.")
for i in range(10):
        th = Thread(target=sleepFun, args=(i, ))
        th.start()
        time.sleep(1)
res=calculation()
print("Res=",res)
