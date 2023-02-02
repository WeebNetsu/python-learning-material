from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == '__main__':
    pool = Pool() 
    numbers = range(1, 11)

    # pool will automatically allocate number of processes
    # pool will split the below into equal chuncks so it can be done at the same time with processors
    cubed_nums = pool.map(cube, numbers) # we can map over an array with pool... map(func, array)
    print(cubed_nums)

    # execute 1 function (by not mapping over array)
    cubed_number = pool.apply(cube, args=(numbers[-1], ))
    # NOTE: There are more methods in the docs
    print(cubed_number)

    pool.close() # closes the pool
    pool.join() #finishes using pool before continuing with main thread