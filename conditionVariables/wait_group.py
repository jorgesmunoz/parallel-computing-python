from threading import Condition


class WaitGroup:
    wait_count = 0
    cv = Condition()

    def add(self, count):
        WaitGroup.cv.acquire()
        WaitGroup.wait_count += count
        WaitGroup.cv.release()

    def done(self):
        WaitGroup.cv.acquire()
        if WaitGroup.wait_count > 0:
            WaitGroup.wait_count -= 1
        if WaitGroup.wait_count == 0:
            WaitGroup.cv.notify_all()
        WaitGroup.cv.release()

    def wait(self):
        WaitGroup.cv.acquire()
        while WaitGroup.wait_count > 0:
            WaitGroup.cv.wait()
        WaitGroup.cv.release()
