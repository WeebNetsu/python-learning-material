# Tutorial: You don't have to make a tutorial about this, you can if you want to tho
from multiprocessing import Process, Array, Lock
import time


def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for j in range(len(numbers)):
            with lock: # to keep processes from accessing the same variable at the same time
                numbers[j] += 1



if __name__ == '__main__':
    shared_array = Array('d', [0.0, 100.0, 200.0]) # d = double
    print(f"Number at beginning is {shared_array[:]}")
    lock = Lock()

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Number at end is {shared_array[:]}")
