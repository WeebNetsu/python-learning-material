from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b)  # creates a product of both lists
# prod = product(a, b, repeat=2) # allows you to repeat everything
print(list(prod))

print("")

#permutations
a = [1, 2, 3]
# perm = permutations(a)
perm = permutations(a, 2)  # limits amount of items per permutation
print(list(perm))  # displays all the ways the list can be ordered

print("")

#combinations
# same as permutations, but adding a length is manditory and there are no duplicates
comb = combinations(a, 2)
print(list(comb))
# will do the same as combinations, but will add stuff like (1, 1), (2, 2) etc.
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

print("")

#accumulate
acc = accumulate(a)
# 1, 3, 6 -> 1, 1+2, 1+2+3
print(list(acc))
acc = accumulate(a, func=operator.mul)  # will multiply instead of add
print(list(acc))

print("")


# groupby
def less_than_9(val):
    return val < 9


a = [12, 1, 4, 17, 6, 20]
# creates an object where everything smaller than 9 has a key of true
group_obj = groupby(a, key=less_than_9)

for key, val in group_obj:
    print(key, list(val))

#count
# creates an infinite loop that starts at 10
for i in count(10):
    print(i)

    if i == 15:
        break

#cycle
a = [1, 2, 3, 4, 5]
# prints all values inside the list 'a', over and over, forever
# for i in cycle(a):
#   print(i)

#repeat
# repeat the value inside repeat forever
# for i in repeat(5):
# print(i)

# tell it when to stop
for i in repeat(7, 10):  # only repeat 10 times
    print(i)
