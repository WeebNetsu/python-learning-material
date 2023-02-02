# chr converts a *positive* integer to its corrosponding alphabetical value
# basically converting from ascii to alphabed
print(chr(65)) # A
print(chr(97)) # a
print(chr(120)) # x
print(chr(95)) # underscore

# ord converts alphabetical characters to their corrospoding integeger values
# so converting from alphabed to ascii
print(ord('a')) # 97
print(ord("A")) # 65
print(ord("?")) # 63

# You can loop through the alphabed using ord (it may only work in Python3)
for letter in range(ord("A"), ord("Z") + 1):
    print(chr(letter))