import time

start = time.perf_counter() # counts time it takes to execute script

def do_something():
    print("sleeping for 1 second")
    time.sleep(1) # sleeps for 1 second
    print("done sleeping")

do_something()
do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")