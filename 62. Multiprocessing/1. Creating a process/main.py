"""
A process is an instance of a program (like 1 firefox browser = 1 process)
multiprocessing takes advantage of multiple CPU's and cores (great for CPU bound processes)
processes doesn't share memory (eg. sublime text won't share it's memory with vscode)
processes starts independantly of other processes

A process requires more memory (than a thread). It will also require more time to start up (than a thread)
Since processes don't share memory inner process communication (when 2 or more processes communicate with each other) can be complicated
"""

from multiprocessing import Process # to do multi processing
import os, time

def demanding_process():
    for i in range(1000):
        i * i
        # time.sleep(0.1) # to see the processes happening

processes = [] # all processes will be stored here
num_processes = os.cpu_count() # number of cpus on your machine = number of processes that can run

# create processes
for i in range(num_processes):
    # target = object/function to be executed by process
    # args = any arguments that should be passed in (in tuple form)
    p = Process(target=demanding_process)
    processes.append(p)

# start processes
for p in processes:
    p.start()

# join processes
for p in processes:
    # basically means that you want to wait for processes to finish before continueing the main thread
    p.join()

print("This is the end of the main process")