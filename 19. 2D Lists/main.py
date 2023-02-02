lists = [ # 2D array/list
	[1, 2, 3], # grid-like structure
	[4, 5, 6],
	[6, 7, 8]
]

print(lists[0][1]) # 2 
print("")

for row in lists:
	print(row)
	for column in row:
		print(column) # prints everything out