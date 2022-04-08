from threading import Thread, Lock
import time


class StingySpendy:
    money = 100
    mutex = Lock()

    def __init__(self) -> None:
        pass

    def stingy(self):
        for i in range(1000000):
            StingySpendy.mutex.acquire()
            StingySpendy.money += 10
            StingySpendy.mutex.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(1000000):
            StingySpendy.mutex.acquire()
            StingySpendy.money -= 10
            StingySpendy.mutex.release()
        print("Spendy done")


ss = StingySpendy()
t_stingy = Thread(target=ss.stingy, args=()).start()
t_spendy = Thread(target=ss.spendy, args=()).start()
time.sleep(5)

print(f"Money in the end {ss.money}")
