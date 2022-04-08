from ast import arg
import time
from threading import Thread


# Child Thread
def child():
    print("Child Thread doing work...")
    time.sleep(5)
    print("Child Thread done...")

# Parent Thread


def parent():
    t = Thread(target=child, args=())
    t.start()
    print("Parent Thread is waiting Thread child...")
    # Lock Parent Thread until the child finishes
    t.join()
    print("Parent Thread is unlocked...")


parent()
