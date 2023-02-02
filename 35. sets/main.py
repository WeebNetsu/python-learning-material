# sets are unordered, has no duplicates but are mutable

test = {1, 2, 2, 1, 3}
test = set([1, 2, 2, 1, 3]) # this is the same as the above code
test = set("Hello World") # can make a set from a string
print(test)

examp = {} # this is an dictionary, not a set
examp = set() # this is an empty set

examp.add(2) # add element to set
examp.add(5)
examp.add(9)

# if the element does not exist in the set, this will raise a KeyError
examp.remove(5) # removes element from set
examp.discard(2) # removes element from set BUT does not return an error if element was not found
examp.discard(1) 
print(examp)

examp = set([1, 2, 3, 4, 5, 6])
examp.clear() # empties the set
print(examp)

examp = set([1, 2, 3, 4, 5, 6, 7])
# removes the first element from set and returns the value
print(examp.pop(), "\n", examp)

for i in examp: # loop over set
    print(i)

if 2 in examp: # check if element exists in set
    print("2 does exist in the set")

odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

union = odd.union(even) # merges the 2 sets
print(union)

# only returns the values that exists in BOTH sets
intersect = odd.intersection(prime)
print(intersect)

setOne = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setTwo = set([1, 4, 7, 9, 14, 29])

# only return the values that do NOT occure in both sets
diff = setOne.difference(setTwo)
print(diff)

# return the values that are in sets one and two but not the values that are in both sets
diff = setOne.symmetric_difference(setTwo)
print(diff)

setOne.update(setTwo) # adds the elements in setTwo into setOne
print(setOne)

# only adds the elements to setOne that was part of BOTH setOne and setTwo
setOne.intersection_update(setTwo)
print(setOne)

setOne = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setTwo = set([1, 4, 7, 9, 14, 29])

# returns the values in setOne that does NOT exist in setTwo
setOne.difference_update(setTwo)
print(setOne)

setOne = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setTwo = set([1, 4, 7, 9, 14, 29])

# return the values that are in sets one and two but not the values that are in both sets
setOne.symmetric_difference_update(setTwo)
print(setOne)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# returns if setB is a subset of setA (does setB exist in setA)
print(setB.issubset(setA))
# returns if setA contains all elements of setB
print(setA.issuperset(setB))
# returns true if setA and setB do not contain the same elements (setB is NOT a subset or superset of setA)
print(setA.isdisjoint(setB)) # false
print(setA.isdisjoint([10, 12, 14])) # true

setB = setA # copies setA BUT setA now gets modified when setB gets modified
setB.add(10) # adds 10 to setA AND setB
setC = setA.copy() # copies a new set
setC.add(99) # adds 99 to only setC
print(setA, "\t", setC)

constantSet = frozenset([1, 2, 3, 4, 5]) # a set that cannot be mutated