# There are 3 ways to format a string
name = "Micheal"
age = 30
money = 43.98542
# %s -> string
# %d -> diget/number
# %f -> floating point value
# Note: %f has a default limit of 6 digets after the "."
# You can increase/deacrease this with %.2f - tis will limit it to 2 digits
text = '%s is %d years old and has R%.2f in his wallet' % (name, age, money) 
print(text)

# note for formatting floats you now use ":" instead of "%"
text = "{} is {} years old and has {:.4f} in his wallet".format(name, age, money)
print(text)

# new feature since Python 3.6
text = f"{name} is {age} years old and has {money:.2f} in his wallet"
print(text)