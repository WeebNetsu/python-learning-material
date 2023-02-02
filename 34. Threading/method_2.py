import threading # allows threading
import time

start = time.perf_counter() # counts time it takes to execute script

def do_something(seconds):
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds) # sleeps for 1 second
    print("done sleeping")

threads = list() # list of threads running

for _ in range(10): # create multiple threads at once
    thread = threading.Thread(target=lambda:do_something(1))
    thread.start()
    # since you cant use thread.join() in this loop 
    # (since it will make the thread execute before it finishes looping)
    # you have to append the threads to a list
    threads.append(thread)

for thread in threads:
    thread.join() # now you can join all of them

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds") # finishes in 1 second