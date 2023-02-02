from threading import Thread, Lock, current_thread # allows us to see the current thread
# fifo - first in, first out (first thread finishes first)
from queue import Queue
import time


""" how_queues_work:
q = Queue()

q.put(1)
q.put(2)
q.put(3)

first = q.get()  # returns first item in queue
print(first)  # 1
q.task_done()  # tell python that you're done with the task
second = q.get()  # gets second item in queue
print(second)  # 2
q.task_done()

q.join()  # block the main method until queue has been completed

if q.empty():  # true if queue is empty
    print("queue is empty") """

def worker(q, lock):
    while True: # thread.daemon kills this while loop when the main process ends
        value = q.get()

        with lock: # to keep the queues from printing out at the same time
            print(f"Thread: {current_thread().name} (Value: {value})")
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True # daemon is pronounced demon
        thread.start()

    for i in range(20):
        q.put(i)
    
    q.join()

    print("Main end")
