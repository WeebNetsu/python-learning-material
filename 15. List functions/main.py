lucky_numbers = [2, 17, 7, 10, 77, 70]
friends = ["Bak", "Lawrence", "Willem", "Jean"]

friends.append("Jesse") # adds to the end of the list
print(friends)

# insert value into specific index inside friends list
friends.insert(4, "Lucah")
print(friends)

friends.remove("Willem") # remove element in list
print(friends)

friends.pop() # removes last element in list
print(friends)

print(friends.index("Jean")) # returns index of element if exist in list (else get error)

friends.append("Lucah")
friends.append("Lucah")
friends.append("Lucah")
friends.append("Lucah")

print(friends.count("Lucah")) # returns amount of duplicates of "Lucah" is in list

print(lucky_numbers)
lucky_numbers.sort() # sorts list (ascending order)
print(lucky_numbers)
lucky_numbers.reverse() # reverses the current order of the list
print(lucky_numbers)
new_list = sorted(lucky_numbers) # sorted is not permanent like .sort()
print(new_list)
print(lucky_numbers)

# note: using list1 = list2 will mean that if you modify list1, then list 2 will change as well
friends2 = friends.copy() # copies another list
print(friends2)
friends2 = list(friends) # same as friends.copy()
friends2 = friends[:] # same as friends.copy

friends[0] = "Lady Macbeth" # replaces item at index 0 (Bak)
print(friends)

print(lucky_numbers + [19, 1, 0, 24])
print(lucky_numbers * 5) # string manipulation procedures works on lists

print(7 in lucky_numbers) # returns true if element exists inside list
print(not "Jean" in friends) # returns true if element DOES NOT exist inside list

print(len(lucky_numbers)) # returns length of list

# adds list lucky_numbers to the list friends
friends.extend(lucky_numbers)
print(friends)

friends.clear() # empties the list
print(friends)

print()

new_list = [0] * 5 # adds 5 0's to the list
print(new_list)
extra_list = [1, 2, 3, 4, 5, 6]
combined_list = new_list + extra_list # adds 2 lists together
print(combined_list)

print(combined_list[3:7]) # copies items in index 3, 4, 5, 6
print(combined_list[0::2]) # coppies all 2nd items from index 0

num_list = [1, 2, 3, 4, 5]
sqr_list = [i * i for i in num_list] # copies everything in num_list and squares it
print(sqr_list)