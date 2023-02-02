words = ["ten", "girl", "magnet", "pokemon", "dad"]
		# 0(-5)  1(-4)    2(-3)     3(-2)     4(-1)
print(words[0]) # prints ten
print(words[4]) # prints dad
print(words[-1]) # prints dad
print(words[2:]) # prints everything from index 2
print(words[2:4]) # prints everything from index 2 to 4
print(words) # displays everything in list

words2 = ["mommy", "lilly", "liver", "cat"]
words_combined = words + words2 # adds 2 lists togeter
print(words_combined)

empty_list = [] # empty list
empty_list2 = list() # alternative method to create an empty list
print(empty_list)

value_list = [1, "two", 3, 4, "five", False, True, 8.0] # list can contain multiple data types

multi_list = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(multi_list[0][0]) # 1
print(multi_list[-1][2]) # 9
print(multi_list[1][1]) # 5

complicated_list = [ #dont be scared list it out if it's difficult to read
	[ 
		[20, 10, 0], 
		[15, 5, 0] 
	], 
	[ 
		[30, 0, 12], 
		[19, 9, 3] 
	], 
	[ 
		[1, 2, 4] 
	] 
]

print(complicated_list[0][0][0]) # 20
print(complicated_list[0][1][2]) # 0