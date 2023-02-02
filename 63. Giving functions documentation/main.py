def my_cool_func(x: int) -> str: 
	# the above is typing, it doesn't actually do anything, it just helps with documentation
	# the typing is also optional
	"""
	This is just a test function and it is very cool!

	Note i am also cool... We're adding documentation

	Arguments:
		Any number of type integer

	Return:
		Returns the value of x with "The value is " prepended
	"""
	return f"The value is {x}"

help(my_cool_func)