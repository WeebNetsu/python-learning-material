# Note: tuple is basically a list/array, but cannot be changed (constant)
# a reason you'd want to use a tuple over a list is because a tuple is much smaller than a list in size
# which means tuples are faster than lists

myTuple = ("Max", "Jarrod", "Liam")
print(myTuple)
# myTuple[0] = "Josh" -> will cause error
myTuple2 = "Jack", "Neil", "Penny"  # () are optional with tuples
print(myTuple2)

myTuple3 = ("Netsu")  # this is seen as a string, not a tuple
print(type(myTuple3))

myTuple4 = ("Netsu",)  # this is seen as a tuple
print(type(myTuple4))

myTuple5 = tuple(["This", "will", "Change", "into", "a", "tuple"])
print(myTuple5)

print(myTuple[0])  # get elements like normal list/array
print(len(myTuple))  # returns length of tuple

if "Lucah" in myTuple:  # search for something inside tuple
    print("Found Lucah!!!")
else:
    print("No such element found!")

myTuple6 = ("a", "p", "p", "l", "e")
print(myTuple6.count("p"))  # counts amount of same items in tuple
print(myTuple6.index("l"))  # finds the index of element in tuple

myTuple7 = ("Marly", 24, "Developer")
name, age, job = myTuple7  # assignes variables according to values in tuple
print(name, age, job)

myTuple8 = [1, 2, 3, 4, 5, 6, 7]
i1, *i2, i3 = myTuple8  # places items inside i2 if there are more items than variables
print(i1, "\t2:", i2, "\t3:", i3)

# can use tuple format to assign multiple variables
(tup1, tup2) = ("Josh", 10)
print(tup1)
tup1 = 22  # normal string
print(tup1)

myDict = {
    "name": "Jack",
    "age": 25,
    "skills": ["Python", "Photoshop"]
}
toTuple = myDict.items()  # .items() returns all the items in a dictionary
print(toTuple)

tup_a = (5, 9, 10)
tup_b = (0, 8, 20)
# the below will only compare the 1st items in the tuples. If both the first items are
# the same, then the second items will be compared
print(tup_a > tup_b)

tup_c = (5, 5, 12)
tup_d = (5, 6, 10)
print(tup_c > tup_d)
