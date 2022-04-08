from threading import Thread, Lock, Condition
import time


class StingySpendy:
    money = 100
    cv = Condition()

    def __init__(self) -> None:
        pass

    def stingy(self):
        for i in range(1000000):
            StingySpendy.cv.acquire()
            StingySpendy.money += 10
            StingySpendy.cv.notify()
            StingySpendy.cv.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(500000):
            StingySpendy.cv.acquire()
            while StingySpendy.money < 20:
                StingySpendy.cv.wait()
            StingySpendy.money -= 20
            if StingySpendy.money < 0:
                print(f"Money in bank {StingySpendy.money}")
            StingySpendy.cv.release()
        print("Spendy done")


ss = StingySpendy()
t_stingy = Thread(target=ss.stingy, args=()).start()
t_spendy = Thread(target=ss.spendy, args=()).start()
time.sleep(5)

print(f"Money in the end {ss.money}")
