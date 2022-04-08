import os
from os.path import isdir, join
from threading import Thread, Lock

mutex = Lock()
matches = []


def file_search(root, filename):
    print(f"Searching in: {root}")
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)  # concatenate root with file
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            # Recursive method (calls the same function)
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)

    for t in child_threads:
        t.join()


def main():
    t = Thread(target=file_search, args=("/home/jorge", "README.md"))
    t.start()
    t.join()
    for match in matches:
        print(f"Matched: {match}")


main()
