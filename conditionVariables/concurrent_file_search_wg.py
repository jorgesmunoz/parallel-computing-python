from multiprocessing.connection import wait
import os
from os.path import isdir, join
from threading import Thread, Lock
from wait_group import WaitGroup

mutex = Lock()
matches = []


def file_search(root, filename, wait_group):
    print(f"Searching in: {root}")
    for file in os.listdir(root):
        full_path = join(root, file)  # concatenate root with file
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            # Recursive method (calls the same function)
            wait_group.add(1)
            t = Thread(target=file_search, args=(
                [full_path, filename, wait_group]))
            t.start()

    wait_group.done()


def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t = Thread(target=file_search, args=(
        ["/home/jorge", "README.md", wait_group]))
    t.start()
    wait_group.wait()
    for match in matches:
        print(f"Matched: {match}")


main()
