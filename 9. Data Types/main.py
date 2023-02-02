# show exaple
string = "Hello World";
integer = 20;
floating_point = 3.14159;
boolean = True;
null = None

# dont show exaple (but tell it exists in tutorial)
list_value = ["apple", "cherry", "pear"]; # array
tuple_value = ("apple", "cherry", "pear"); # constant, cannot be edited

dict_value = {
	"name": "John",
	"age": 22
}

# NOT IN TUTORIAL
bytes_value = b"Hello";
byte_array = bytearray(5);
memory_view = memoryview(bytes(5)); # displays place in memory
set_value = {"apple", "cherry", "pear", "apple"}; # array that cannot hold duplicates
frozenset_value = frozenset({"apple", "cherry", "pear"}); # set, but cannot be mutated (constant)
range_value = range(6); # all numbers from 0 - 5
complex_value = 1j;
print(type(complex_value)); #get data type

# to set a specific data type, add the data type to begining
x = str("string");
y = int(24);
z = dict({
	"name": "Lossy",
	"age": 99
})

print(memory_view);
print(set_value);
print(dict_value["name"]);
print(range_value);
