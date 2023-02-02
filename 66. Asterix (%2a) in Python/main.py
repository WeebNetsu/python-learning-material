# *args = take in any number of arguments
# **kwargs = take in a keyword argument

def example(a, b, *args, **kwargs): # note: args and kwargs are optional when calling the function
    print(a, b)

    for arg in args:
        print(arg)

    for key in kwargs: # kwargs is a dict
        print(f"{key}: {kwargs[key]}")

#example (a, b, *args1, *args2, *args3, **kwargs1, **kwargs2)
example(12, 2, 4, 5, "six", one=1, two=2)

# without *args
example(2, 3, one=1, two=2)

# without **kwargs
example(2, 3, 99, 22)

def example_two(a, b, *, c, d): # all parameters after the * should be a keword argument
    print(a, b, c, d)

# example_two(1, 2, 3, 4) # will throw error
example_two(1, 2, c=3, d=4)

def example_three(*args, last): # last is a keyword argument since it is after *args
    for arg in args:
        print(arg)
    print(last)

example_three(1, 2, 3, last=4)

def myfunc(a, b, c):
    print(a, b, c)

mylist = [2, 4, 6]
myfunc(*mylist) # the * unpacks the list so: [2, 4, 6] -> 2, 4, 6 (this also works with tuples)

mydict = {
    'a': 3,
    'b': 6,
    'c': 9
}
myfunc(**mydict) # unpacks the dictionary (note: keys should be the same as the arguments in the function (so a, b, c in this case))
# the above is the same as: myfunc(a=3,b=6,c=9)