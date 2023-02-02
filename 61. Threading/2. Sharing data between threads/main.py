from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value

    lock.acquire() # blocks threads from using the same variable at the same time

    local_copy = database_value # save data from database in local copy
    local_copy += 1 # add to it
    time.sleep(0.1) # emulating a process that will take some time to complete (python will intelegently switch to other thread)

    database_value = local_copy # give the database its new data

    lock.release() # releases lock, allowing other threads to use the same variable

    """
    The above can also be done like this:
    with lock:
        local_copy = database_value # save data from database in local copy
        local_copy += 1 # add to it
        time.sleep(0.1) # emulating a process that will take some time to complete (python will intelegently switch to other thread)

        database_value = local_copy # give the database its new data
    """

if __name__ == '__main__':
    lock = Lock() # prevents another thread from accessing the same variable at the same time another thread is using it

    print(f"start value: {database_value}")

    thread1 = Thread(target=increase, args=(lock,))    
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"end value: {database_value}") # will be 1
    """
    The output is 1 (if lock was not used) and not 2 because the 2 threads were trying to modify the same variable at the same time
    """
    print("Main end")