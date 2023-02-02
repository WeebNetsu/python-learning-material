"""
A thread is an entity in a process, so a piece of code running seperately from the main process
All threads inside a process shares memory 
Threads can easily communicate with each other
Great for Input and Output type tasks (can do something else while waiting for a process to respond)

Threads are limited by GIL (Global interpreter lock) so only one thread can be run at a time
bad for CPU-bound tasks since only one thread can run at a time
Cannot be interrupted/killed (memory leak problems)
memory leaks: When objects are not released from memory (RAM) after being used
"""

from threading import Thread
import time

def square():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':
    threads = []
    num_threads = 10 # set a number you want

    for i in range(num_threads):
        # the below can also take in an args=
        thread = Thread(target=square)
        threads.append(thread)

    for t in threads:
        t.start() # start threads

    for t in threads:
        t.join() # wait for thread to finish before continuing with the main thread
        print("here")

    print("End of file")