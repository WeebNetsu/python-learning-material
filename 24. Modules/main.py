import random # import a module (code someone else wrote)

for x in range(5):
	print(random.randint(1, 10)) # prints a random number between 1 and 10 (both included)

from math import pi, sqrt # import something specific instead of the whole module

print(pi) # prints Pi (3.14159...)
print(sqrt(25)) # prints 5

from math import * # imports everything from a module (bad practise)
from math import sqrt as square_root # imports and gives it a new name

print(square_root(100)) # 10

import random as r
print(r.randint(1, 10)) # prints a random number between 1 and 10