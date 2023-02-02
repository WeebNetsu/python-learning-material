import concurrent.futures # newer version of threads
import time

start = time.perf_counter() # counts time it takes to execute script

def do_something(seconds):
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds) # sleeps for 1 second
    return "done sleeping"

with concurrent.futures.ThreadPoolExecutor() as executor:
    # The below shows you how to threads with 1 item
    # feature1 = executor.submit(do_something, 1)
    # print(feature1.result())

    results = [executor.submit(do_something, 1) for _ in range(10)]
    # do a map instead if you want:
    # results = executor.map(do_something, [5, 4, 3, 2, 1])
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds") # finishes in 1 second