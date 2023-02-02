import asyncio, time

"""
Syncronus programming:
    Bunch of statements executed in sequence, so one statement has to finish before another can execute
    EXAMPLE:

        def hello():
            return "hello"

        hello()
        print("Welcome")

    In the above example hello() will be executed before print(), this is syncronus

Asyncronous programming:
    Basically like multi-threading, when a piece of code waits for something such as a download to complete
    the other code can continue with their business while they wait for the first piece of code to finish
"""


async def main():  # asyncronous function
    print("Hello World")

    # await has to be inside an async funtion to work
    # await allows you to run a co-routine
    # await say_something("Hello!!!!") # this is a valid way to run an async function
    task = asyncio.create_task(say_something("Hello!!!!!")) # creates a task that if wating will let the other code execute first
    # by putting await here it will BLOCK the rest of the code from running until it has finished executing
    # without the await keyword the rest of the code will continue executing while we wait for say_something() to finish
    # await task 

    # this code should finish before continuing with the rest, this will allow say_something() to finish
    # since it has to wait for us. if we just used time.sleep() we would've had to wait for this function
    # to finish before allowing say_something() to continue/finish
    await asyncio.sleep(2) 
    print("Goodbye") # since the above is a task, when it sleeps this piece of code will be executed

    # NOTE: say_something() will only be executed when something is being await(ed)


async def say_something(text):
    print(text)

    await asyncio.sleep(1)  # asyncronous way to sleep program
    # time.sleep(20)

# asyncio.run(main())  # adds the async main() to the async co-routine and runs it

async def fetch_data():
    print("Fetching....")
    await asyncio.sleep(1)
    print("Done Fetching")
    
    return { "data": 1 }

async def print_nums():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def executor():
    task1 = asyncio.create_task(fetch_data()) # REMEMBER: This returns something
    task2 = asyncio.create_task(print_nums())

    # the below will wait for task1 to finish, then return whatever value it had into the variable
    # if you don't await it, you'll get a task retunred and not the return value
    value = await task1 
    print(value)
    # NOTE: if you don't await for a function, then as soon as the main thread ends that function,
    # wether it is done or not will also end
    # so if you remove the below code, then the print_nums() will not finish executing
    await task2

asyncio.run(executor())