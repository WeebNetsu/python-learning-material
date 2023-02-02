from fractions import Fraction

a = Fraction(6, 2) # 6 / 2
print(a)

b = Fraction(5, 4)
print(a + b) # 17 / 4
print(a * b) # 15 / 4

c = a * b
print(c.numerator) # get numerator (15)
print(c.denominator) # get denominator (4)
print(c.limit_denominator(3)) # limits the size of the denominator to 3

x = 3.5
y = Fraction(*x.as_integer_ratio()) # convert to fraction
print(y) # 7 / 2