import threading # allows threading
import time

start = time.perf_counter() # counts time it takes to execute script

def do_something():
    print("sleeping for 1 second")
    time.sleep(1) # sleeps for 1 second
    print("done sleeping")

# create thread(s)
thread1 = threading.Thread(target=do_something)
thread2 = threading.Thread(target=do_something)

# start threads
thread1.start()
thread2.start()

'''
The below code is OPTIONAL, it insures that the threads finish executing before 
moving on to the code below it, otherwise the output would be:
>>> sleeping for 1 second
>>> sleeping for 1 second
>>> Finished in 0.02 seconds
>>> done sleeping
>>> done sleeping

instead of:
>>> sleeping for 1 second
>>> sleeping for 1 second
>>> done sleeping
>>> done sleeping
>>> Finished in 1.00 seconds
'''
thread1.join()
thread2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")