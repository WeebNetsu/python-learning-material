x = 3.14159

print(format(x, "0.2f")) # rounds to 2 decimals
print(format(x, "0.3f")) # rounds to 3 decimals

print("value is {:0.4f}".format(x)) # format directly in a string

x = 17701.34598
# format and JUSTIFY (align) text with </>/^
print(format(x, ">10.2f")) # justify with 10 spaces to the right to 2 decimals
print("this is {:<10.2f}justified left".format(x))
print("this is{:^20.3f}justified both left and right".format(x))

x = 1990134235.12234
print(format(x, ",")) # add a thousands seperator
print(format(x, ",.2f")) # add a thousands seperator and format
