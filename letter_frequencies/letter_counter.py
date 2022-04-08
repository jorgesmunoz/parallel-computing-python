import json
from threading import Thread, Lock
import urllib.request
import time

finished_count = 0


def count_letters(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    text = str(response.read())
    mutex.acquire()
    for l in text:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1
    mutex.release()


def main():
    frequency = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0

    start = time.time()

    for i in range(1000, 1020):
        t = Thread(target=count_letters, args=(
            f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()

    # Check if a thread has finished or not

    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        # time.sleep(0.5)

    end = time.time()

    print(json.dumps(frequency, indent=4))
    t = end - start
    print(f"Done, time taken {t}")


main()
