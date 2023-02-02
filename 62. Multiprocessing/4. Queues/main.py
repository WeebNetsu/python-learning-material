from multiprocessing import Process, Queue

def square(numbers, q):
    for i in numbers:
        q.put(i * i)

def make_negative(numbers, q):
    for i in numbers:
        q.put(-1 * i)

if __name__ == '__main__':
    q = Queue()
    numbers = [1, 2, 3, 4, 5]
    # print(f"Number at beginning is {shared_array[:]}")

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    # print(f"Number at end is {numbers[:]}")
