# if you make a tutorial, just make it, I customized it as much as possible (so no plagerism)
"""
A function decorator is something that takes in a function and then extends the 
functionallity of that function
"""

import functools  # this allows us to let the funtions keep their original identity


def mydecorator(func):
    def wrapper():
        # do something before exec uting the function
        print("Something before the function")

        func()  # execute the function

        # do something after executing the function
        print("After the function")

    return wrapper  # return the wrapper function


def say_hello():
    print("Hello")


say_hello()  # normal function
print()

say_hello = mydecorator(say_hello)  # using a decorator
say_hello()

print()


@mydecorator  # the same as saying: whoami = mydecorator(whoami)
def whoami():
    print(f"You are Jack")


whoami()

print()


def dec(func):
    # lets the input function keep its original identity
    @functools.wraps(func)
    # *args and **kwargs are optional, but allows you to add any amount of arguments to the function
    def wrapper(*args, **kwargs):
        print("BEFORE")
        # since the function passed in returns something, we need to store that value
        res = func(*args, **kwargs)
        # note: anything after will now be done after res has been set, but
        # res will be returned at the end and not the middle
        print("AFTER")
        return res

    return wrapper


@dec
def sum(x, y):
    return x + y


x = sum(5, 2)
print(x)

print()

# help(whoami)  # wrapper (lost identity)
# help(sum)  # sum (did not lose identity)

# print(whoami.__name__)  # wrapper (lost identity)
# print(sum.__name__)  # sum (did not lose identity)


def repeat(num):
    # this can take in the function since repeat takes in its own now
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                # before
                res = func(*args, **kwargs)
                # after
            return res

        return wrapper

    return decorator_repeat


@repeat(num=3)
def say_hi(name):
    print(f"Hi {name}!")


say_hi("Jackson")

print()


# Decorators also exists for classes
class Counter:
    def __init__(self, func):
        self.func = func
        self.num = 0

    # every time the class is called, do the following
    def __call__(self, *args, **kwargs):
        self.num += 1
        print(f"Function has been called {self.num} times")
        return self.func(*args, **kwargs)


@Counter
def print_hello():
    print("Hello")


print_hello()
print_hello()
print_hello()
print_hello()
