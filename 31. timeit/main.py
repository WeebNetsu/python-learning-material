# timit can be used to time stuff
import timeit # imports the timit library
#timeit(stmt=what to create, how many times to do it)
print(timeit.timeit(stmt="[10, 20, True, 'Maggie']", number=10000000)) # how long it takes to create so many lists
print(timeit.timeit(stmt="(10, 20, True, 'Maggie')", number=10000000)) # how long it takes to create so many tuples

print(timeit.timeit(stmt="x = 24", number=10000000))
print(timeit.timeit(stmt="x = 24.0", number=10000000))