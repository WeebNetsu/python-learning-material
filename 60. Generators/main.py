# generator: function that returns iteratible object
# they generate objects one at a time when you ask for it (lazily)

def my_generator():
    yield 1 # yield instead of return
    yield 2
    yield 3 # you can have multiple yield statements

g = my_generator()

for i in g: # loop through all the values in generator
    print(i)

# next(g) # raise a stopiteration error since there is no next value in g (we already itterated over them)

f = my_generator()
val = next(f) # gives you the next value in generator
print(val)
print(next(f))

nums = my_generator()
print(sum(nums)) # prints the sum of all values in the object

sorting = my_generator()
print(sorted(sorting, reverse=True))

def counter(num):
    print("Counter Starting")

    count = 0
    while count <= num:
        count += 1
        yield count

    # the counter will not display this until count == num
    print("Counter Ended")

count = counter(20)
print(next(count))
print(next(count))

for _ in count: # so we can see the end of the counter ("Counter Ended")
    pass

# Normal Function:
def mklist(num):
    nums = [] # you need to create a list (which will require more memory)
    item = 0

    while item < num:
        item += 1
        nums.append(item)

    return nums

# generator version
def mklist_gen(num):
    item = 0 # you don't need a list (less memory needed)

    while item < num:
        item += 1
        yield item

# basically, generators are better on memory than normal functions
print(sum(mklist(20)))
print(sum(mklist_gen(20)))

gen = (i for i in range(10) if i % 2 == 0) # shorthand for generator
norm = [i for i in range(10) if i % 2 == 0] # normal shorthand for list

for i in gen:
    print(i)

print(norm)