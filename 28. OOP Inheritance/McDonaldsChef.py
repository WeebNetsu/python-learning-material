from Chef import Chef # import class Chef

# since we're extending/inheriting, we can use all the existing functions and more
class McDonaldsChef(Chef): # inherits from class Chef now
	def __init__(self, yearsOfService, burgersMade, headChef):
		super().__init__(yearsOfService, burgersMade)
		"""
			The above code implements the yearsOfService and burgersMade parametes
			that the PARENT class already initialized, so we dont have to say:
			self.yearsOfService = yearsOfService
			self.burgersMade = burgersMade
			(since it was already said in the parent class [Chef])
		"""
		self.headChef = headChef # headChef is a new parameter added to this class
		

	def make_special_dish(self): # can overrite exsisting function
		print("The chef made pizza")

	def make_burger(self): # add new functions
		print("The chef made a burger")