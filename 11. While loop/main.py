i = 1
while i <= 3: # normal while loop
	print(i)
	i += 1 # can't use i++
print("Finished!")

i = 1;
while True: # infinite loop
	i += 1
	if i == 5:
		break # ends the loop
print("infinate loop ended");

i = 0
while i < 3:
	i += 1
	if i == 2:
		continue; # skips the rest of the code and goes back to the top
	print(i);