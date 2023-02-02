hello = ["hello", "hallo", "hola", "konnichiwa", "oi"]

for i in range(1, 10):
	print(i) # prints values 1-9

for word in hello: # stores current value inside word
	print(word) # prints each value

string = "testing to make sure"
count = 0
for x in string: # loops through string
	if x == 't': # if string[x] == 't' then
		count += 1 # increment count by 1 (counts number of 't's) 
print(str(count) + " 't's exist inside variable string")
	
for index, word in enumerate(hello, start=0): # you can say where index starts at
	print(index, word)

for x in range(1,10): # counts from 1-9
	print(x) # prints: 1, 2, 3, 4, 5, 6, 7, 8, 9

names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

# loops through multiple lists(arrays) at once
for name, hero, universe in zip(names, heroes, universes): 
	print(f"{name} is {hero} from {universe}") # format version of print