import random # to generate random numbers

print(random.random()) # random float between 0 and 1
print(random.uniform(1, 10)) # random float between 1 and 10
print(random.randint(1, 10)) # random integer between 1 and 10 (including 10)
print(random.randrange(1, 10)) # random int between 1 and 10 (excluding 10)
print(random.normalvariate(0, 1)) # random float somewhere between -1 and 1

a = list("abcdefghijklmno")
print(random.choice(a)) # pick random item from list
print(random.sample(a, 3)) # pick 3 random items from the array (no duplicates)
print(random.choices(a, k=3)) # pick random item from list (include duplicates)
random.shuffle(a) # will shuffle a list
print(a)

# the below will keep the random numbers the same (different seeds = different random numbers)
random.seed(1)
print(random.randint(1, 10))
random.seed(1)
print(random.randint(1, 10))

# the above should not be used for security!
# use the below instead

import secrets # creates more "true" random values

# secrets takes more time to generate a random value, security = yes
# random is faster than secrets, speed = yes

print(secrets.randbelow(10)) # random number between 0 & 10

print(secrets.randbits(4)) # will generate random number between 0 & 15
# note: the above generates random number from bits

b = list("abcdefghijklmno")
print(secrets.choice(b)) # same as random.choice but not repreducable

# DONT DO BELOW IN TUTORIAL
# python3 -m pip install numpy
import numpy as np

print(np.random.rand(5)) # returns array with 5 random float values
print(np.random.rand(5, 3)) # same as above but in dimension of 5x3
print(np.random.randint(0, 10, 1)) # 1D array with random number between 0 & 10
print(np.random.randint(0, 10, (2, 3))) # 2x3 array with random number between 0 & 10

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr) # shuffle numpy array
# above only shuffles the array blocks, not the items inside them
print(arr)

# NumPy also has a seed function
np.random.seed(1)
print(np.random.rand(2, 2))

np.random.seed(1)
print(np.random.rand(2, 2))