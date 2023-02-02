# easy oneliner function
sum = lambda x, y: x+y
# the above is almost the same as this: def sum(x, y): return x+y
print(sum(20, 5))

points = [(1, 2), (9, 1), (5, 7), (4, 3)]
# sorted is inbuilt and sorts via the first element in the tuple
sorted_points1 = sorted(points)
# the lambda allows us to sort it by the second element in the tuple
sorted_points2 = sorted(points, key=lambda x: x[1])

"""
The above code could've been accomplished with this:
def sorts(x):
	return x[1]
sorted_points = sorted(points, key=sorts)
"""

print(points)
print(sorted_points1)
print(sorted_points2)

list1 = [1, 2, 3, 4]
print(list1)
# multiply all the items in list1 by 2
# map(func, array)
list2 = map(lambda x: x * 2, list1)
# above code could've been accomplished with this: list2 = [x * 2 for x in list1]
print(list(list2))

# filter(func, array)
# filter returns what is true (1 & 2 is smaller than 3 in below example)
list3 = filter(lambda x: x < 3, list1)
print(list(list3))

# reduce(func, array)
from functools import reduce
a = [5, 10]
# reduce affects all items in array, the below will multiply everything
# with each other (in this case only 5 * 10) and return the "sum"
b = reduce(lambda x, y: x * y, a)
print(b)