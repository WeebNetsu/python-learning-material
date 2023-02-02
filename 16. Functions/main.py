def sayHello(): # create a function using def
	print("Hello there!")

sayHello()

def sayHello2(name): # makes function take in a parameter
	print("Hello, " + name)

sayHello2("John") #takes in parameter

def sayHello3(name="Tim"): # make function take in optional parameter
	print("Hello, " + name)

sayHello3() # Hello, Tim
sayHello3("Jack")

def whoAmI(age, name="Kian"): # parameters without default value goes first
	print("Your name is " + name + " and you're " + str(age) + " years old")

whoAmI(24, "Nick")
whoAmI(19)

def sum(num1, num2):
	return num1 + num2 # returns given value

print(sum(20, 10))

def execute():
	print("Running")

	return True # breaks out of funtion

	print("Done") # will not be read

x = execute()

if x: # same as saying if execute():
	print("Execute returned true")