# higher order functions are functions that takes in functions
def merge_function(func, func_arg1, func_arg2):
    return func(func_arg1, func_arg2)


def sum(x, y):
    return x + y


print(merge_function(sum, 10, 5))  # returns 15

# def in def


def add_double(func, arg):
    return func(func(arg))  # runs add_10 twice with same argument


def add_10(x):
    return x + 10


print(add_double(add_10, 5))  # 25 -> 10 + 5 = 15; 15 + 10 = 25
