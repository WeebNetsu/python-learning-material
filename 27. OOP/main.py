from Student import Student # from file Student.py import Student class

student1 = Student("Lucah", "Computer Science", 3.1, False)
student2 = Student("Maggie", "Business", 3.8, True)

print(student1.name)
print(student2.major)
print(student2.on_honor_roll())

student2.own_dorm = False # you can add attributes to an object
print(student2.own_dorm)

setattr(student2, "last_name", "Kelly") # alternative method to above code
print(student2.name, student2.last_name)

print(getattr(student2, "major")) # alternative to student2.major