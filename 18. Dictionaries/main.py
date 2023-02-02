monthConversions = {  # almost like JS object
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: 20  # key and value can be of any type
}

print(monthConversions["Dec"])  # December
print(monthConversions.get("Jul"))  # July
# Display message if key not exist
print(monthConversions.get("Ovm", "Key not found"))
print(monthConversions[1])  # 20
del monthConversions[1]  # deletes from dictionary
monthConversions.pop("Dec")  # removes from dictionary
monthConversions.popitem()  # removes last item in dictionary (from Python 3.7 and up)
monthConversions["Jan"] = 24  # replaces the value stored there
print(monthConversions)

# normal dict, just special
myDict = dict(name="Mary", age=28, city="Cape Town")
# the below code adds to dictionary if the key doesn't exist, but if it does
# it overwrites it
myDict["email"] = "maryl@gmail.com"
print(myDict)
if "name" in myDict:  # finds key in dictionary | use not in for oppisite effect
    print(myDict["name"])

for key in myDict:  # loop through dict
    print(key)

for key in myDict.keys():  # loop through dict method 2
    pass

for value in myDict.values():  # loop through dict (values)
    print(value)

for key, value in myDict.items():  # loop through dict (values and keys)
    print(key, ":", value)

# NOTE: the bottom copying method will affect the ORIGINAL dictionary as well!!!!!!
myDict_copy = myDict  # copies myDict

# The below code copies the dictionary into a new variable
# you can now edit them individually
myDict_copy_2 = myDict.copy()
myDict_copy_3 = dict(myDict)  # same as above .copy function

myDict = {"name": "Max", "age": 22, "email": "max@email.com"}
myDict2 = dict(name="Lucas", age=55, city="Boston")
# the below code will change all the values inside myDict to the values in myDict2
# as well as add the new keys
myDict.update(myDict2)
print(myDict)
