import time
from threading import Thread

def myfunc(i):
    print("Starting thread {}" .format(i))
    time.sleep(5)
    print("Finishing thread {}".format(i))

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
    time.sleep(2)


