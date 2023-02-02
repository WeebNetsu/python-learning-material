from collections import Counter, namedtuple, defaultdict, deque

# COUNTER
my_str1 = "I did not do it"
counted = Counter(my_str1)
print(counted)  # returns dict with items in string counted ie. "i": 2
# returns the 2 most common found items in string
print(counted.most_common(2))
print(list(counted.elements()))  # retruns all the elements in dict

# NAMEDTUPLE
# creates person class with name & age attributes
Person = namedtuple("Person", "name, age")
mark = Person("Mark", 18)  # create Person object
print(mark.name)

# DEFAULT DICT
# normal dict, but has a default value if value has not been set
# normal dicts would give key_error if non-existant value found
defdict = defaultdict(int)  # can be int, float, list etc.
defdict['a'] = 55
defdict['b'] = 22
print(defdict['a'])
print(defdict['c'])  # prints 0 since the default int value is 0

# DEQUE
my_deque = deque()
my_deque.append(5)  # adds to end of deque
my_deque.append(2)
my_deque.appendleft(19)  # adds to beginning of deque
print(my_deque)

my_deque.pop()  # removes last element
my_deque.popleft()  # removes first element
print(my_deque)

my_deque.clear()  # removes all elements

my_deque.extend([5, 10, 15, 20])  # adds list to end of deque
my_deque.extendleft([0, -5, -10])  # adds list to beginning of deque
print(my_deque)

# rotates all elements 2 places to the right (negative number to rotate left)
my_deque.rotate(2)
print(my_deque)
