# By default numbers are in base 10 in Python

x = 1234

print(bin(x)) # base 2
print(oct(x)) # base 8
print(hex(x)) # base 16

# if you want to get rid of the 0x/0b/0o in front of all the numbers, format it:

print(format(x, 'b')) # base 2 (binary)
print(format(x, 'o')) # base 8
print(format(x, 'x')) # base 16