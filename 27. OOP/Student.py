class Student:
	# 'self' basically always needs to be included in objects
	def __init__(self, name, major, gpa, on_probation): # constructor
		self.name = name
		self.major = major
		self.gpa = gpa
		self.on_probation = on_probation
		print("Student object created!")

	def on_honor_roll(self): # auxillary function
		if self.gpa > 3.5:
			return True
		else:
			return False