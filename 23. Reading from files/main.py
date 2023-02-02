############################## 1st METHOD ###############################

print("METHOD 1\n")

# r = read from file
# w = write to file
# a = append to file
# r+ = read and write
# wb = binary write
# rb = binary read
tFile = open("myFile.txt", "r") # opens file

print(tFile.read()) # reads the entire file at once

tFile.close() # closes the file

####################### 2nd METHOD ######################################

print("\nMETHOD 2\n")

tFile = open("myFile.txt", "r+") # r+ = read and write permissions

if not tFile.readable(): # checks if file can be read or not
	print("The file \"myFile.txt\" cannot be read")
	exit() # exits the python script

for line in tFile: # loop through the file line by line
	print(line)

tFile.close()

############################# 3nd METHOD ################################

print("\nMETHOD 3\n")

tFile = open("myFile.txt", "r")

sLines = tFile.readlines() # stores lines in an array
print(sLines)

tFile.close()

######################### 4th METHOD ####################################

print("\nMETHOD 4\n")

tFile = open("myFile.txt", "r")

print(tFile.readline()) # reads a line and puts the cursor on the next line
print(tFile.readline())
print(tFile.readline())
print(tFile.readline())

tFile.close()

########################### 5th METHOD ##################################

print("\nMETHOD 5\n")

with open("myFile.txt", "r") as tFile:
	print(tFile.readlines())
	# you no longer have to say tFile.close with this method