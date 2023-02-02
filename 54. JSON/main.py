# Note: the json is original, so you can use it in a tutorial
import json  # to work with json
from json import JSONEncoder  # to decode a class to json

person = {
    "first_name": "Mark",
    "last_name": "Weddington",
    "age": 39,
    "skills": ["HTML", "CSS", "JavaScript", "Drawing"],
    "employed": False,
    "projects": None  # gets converted into null when converted to json
}

# CONVERTING DICT TO JSON
# convert Python dictionary to JSON
# indent will format the output (index=how many spaces = 1 tab)
# separators(end, assign) will change the "," and ":" to whatever you want (not recommended to use)
# sort_keys -> sort alphabetically by the keys
converted = json.dumps(
    person, indent=4, separators=(";", " = "), sort_keys=True)

print(converted)

# PUTING JSON INTO A FILE
new_file = open("new.json", "w")
# put json into file (will automatically convert DICT to JSON)
json.dump(person, new_file, indent=4)
new_file.close()

# CONVERTING JSON TO DICTIONARY
converted = json.dumps(person)  # just to create a new normal json
# convert json to dictionary
non_converted = json.loads(converted)
print(non_converted)

# READING JSON FROM A FILE
file = open("data.json", 'r')
json_stuff = json.load(file)  # will read from file (and convert to dictionary)
file.close()
print(json_stuff)

# WORKING WITH CUSTOM OBJECTS


class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = Human("Jack", 29)


def object_to_json(obj):
    if isinstance(obj, Human):  # check if the object is an instance of the Human class
        return {
            "name": obj.name,
            "age": obj.age,
            "class": obj.__class__.__name__  # will also return the class name
        }
    else:
        print("Object is not part of Human class")
        return  # or raise TypeError("Object is not of type Human")

# THE BELOW IS AN ALTERNATIVE WAY TO DO THE ABOVE


# convert class to json
# default: will use the function used to convert to json
converted_user = json.dumps(user, indent=4, default=object_to_json)
print(converted_user)


class HumanConverter(JSONEncoder):
    def default(self, obj):  # rewrite the default function
        if isinstance(obj, Human):  # check if the object is an instance of the Human class
            return {
                "name": obj.name,
                "age": obj.age,
                "class": obj.__class__.__name__  # will also return the class name
            }
        else:
            return JSONEncoder.default(self, obj)


# you now use cls instead of default
# converted_user = json.dumps(user, indent=4, cls=HumanConverter)
# the below does the same as the above code
converted_user = HumanConverter().encode(user)
print(converted_user)
