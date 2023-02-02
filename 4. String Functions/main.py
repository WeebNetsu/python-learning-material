print("Hello " + "World") #concatination
print("2" + "2") # concats numbers as string (output: 22)
print("lol " * 3) # lol lol lol
string = "My string"
print(len(string)) # returns length of string
print(string.lower()) # makes string lowercase
print(string.islower()) # checks if string is lowercase only
print(string.upper()) # makes string lowercase
print(string.upper().isupper()) # checks if string is only uppercase
print(string[0]) # 'M'
print(string.index("s")) # 3
print(string.index("tri")) 
print(string.replace("string", "New String")) #replaces "string" with "New String"
print(string.startswith("My")) # returns true if string starts with "My"
print(string[::-1]) # reverses the string

name = "           netsu is cool                 "
print(name.capitalize()) # capitalizes string
print(name.find("cool")) # finds word/character in string
print(name.lstrip() + ' totaly') # removes white space on the left of a string
print(name.rstrip() + ' totaly') # removes white space on the right of a string
print(name.strip() + ' totaly') # removes white space on the left & right of a string

my_string = "I, love my waifu"
my_list = my_string.split(",") # converts string into list and uses delimiter
# by default the split() delimiter is a space so my_string.split() would split it at every space
print(my_list)
new_word = ",".join(my_list) # adds the list in as a string
# "add".join(list) the "add" is what will be added when the string is joined with a list
# so ["hey", "there", "my", "friend"] like this:
# " ".join(["hey", "there", "my", "friend"]) => "hey there my friend"
print(new_word)

mah_list = ["a"] * 6 # ["a", "a", "a", "a", "a", "a"]
# THE BELOW IS BAD PRACTISE: {DO NOT SHOW IN TUTORIAL}
my_new_str = ""
for i in my_list:
    my_new_str += i # this creates a new variable every time to manipulate the string

# THE BELOW IS THE GOOD VERSION OF THE ABOVE CODE: {SHOW IN TUTORIAL}
my_new_str = "".join(mah_list)