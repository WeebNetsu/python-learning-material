import re  # imports support for regular expressions

"""
Regular expressions:
^ - matches the beginning of a line
$ - matches the end of a line
. - any character
\s - white space
\S - non-white space (anything but white space)
* - character repeating 0 or more times
*? - character repeating 0 or more times (non-greedy)
+ - character repeating 1 or more times
+? - character repeating 1 or more times (non-greedy)
[aiueo] - matches a character in this set (any one of them)
[^xyz] - matches any character that is NOT in the set
[a-z0-9] - matches all characters in the alphabet and all numbers (range)
( - where string extraction starts
) - where string extraction ends
"""

text = """Hello, my name is Stephen and I am 18 years old. In 2021 I would like to know both Python and C++ better.
Some times I walk around in my room, maybe even talking to my pet tortoise.
I do love my tortoise, they're cute and fun to look at"""

# re.search is like a more advanced version of find()
if re.search("Stephen", text):  # if text contains "Stephen"
    print("Found")

# the above is the same as:
# if text.find("Stephen"):
    # print("Found")

if re.search("^Hello", text):  # if the line starts with Hello
    print("Found")

# the above is the same as:
# if text.startswith("Hello"):
    # print("Found")
print()

movies = ["Zebras: In the wild", "Zulu Culture", "Zack & Cody: The Movie"]
for movie in movies:
    if re.search("Z.*:", movie):  # returns all strings tarting with 'Z' and has a ':'
        print(movie)

print()

# NOTE: For tutorial, please change the bottom code, it was copied
x = ["X-Sieve: GNU Sieve 2.3", "X-DSPAM-Result: Innocent",
     "X-Plane is behind schedule: 2 weeks"]

for i in x:
    # if i starts with "X-" and has NO spaces up until the ":" then print i
    if re.search("^X-\S+:", i):
        print(i)

# re.findall will return the string that was found, not just true or false
a = "My 2 favorite numbers are 19 and 42"
b = re.findall("[0-9]+", a)
print(b)

# greedy matching will always return the bigger of the choices
c = "From: Using the:"
d = re.findall("^F.+:", c) # returns ['From: Using the:'] since it is greedy!
print(d)

e = re.findall("^F.+?:", c) # here we do it in a non-greedy way, so we get: ['From:']
print(e)

f = "Received an email from stevesteacheryt@gmail.com asking us to sponsor him"
g = re.findall("\S+@\S+", f) # non-whitespace + @ + non-whitespace
print(g)
