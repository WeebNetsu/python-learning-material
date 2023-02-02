# APPENDING
# the below code will create a file if it does not exist
tFile = open('myFile.txt', 'a') # a - append
tFile.write("\nMy body is ready\n")
tFile.close()

# REWRITING
tFile = open("myFile2.txt", 'w') # erase everything and rewrite the file
tFile.write("Hello, World!\n")
tFile.close()

# REAWRITING AND READING
tFile = open("myFile3.txt", "r+") # allows you to read and APPEND
tFile.write("SOME NEW TEXT")
print(tFile.readlines())
tFile.close()